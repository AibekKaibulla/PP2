import pygame
import sys
import random
from game.config import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE, FRAME_RATE, SNAKE_COLOR, FRUIT_COLOR, BACKGROUND_COLOR, SCORE_PER_FRUIT, LEVEL_UP_SCORE, SPEED_INCREMENT
from game.utilities import show_text, check_collision, handle_game_over
from db.database import connect_db, get_or_create_user, load_user_level_and_score, save_game_state


class SnakeGame:
    def __init__(self, user_id):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.paused = False
        self.user_id = user_id
        self.connection = connect_db()
        self.cursor = self.connection.cursor()
        self.load_initial_state()

    def load_initial_state(self):
        level, score = load_user_level_and_score(self.cursor, self.user_id)
        self.snake_position = [300, 300]
        self.snake_body = [[300, 300], [290, 300], [280, 300]]
        self.fruit_position = self.get_random_position()
        self.fruit_spawn = True
        self.score = score
        self.level = level
        self.speed = FRAME_RATE + (self.level - 1) * SPEED_INCREMENT
        self.direction = 'RIGHT'
        self.change_to = self.direction

        show_text(self.screen, f'Loaded Level: {self.level}', (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), font_size=30)
        pygame.display.flip()
        pygame.time.wait(2000)

    def show_pause_screen(self):
        self.screen.fill((50, 50, 50))  # Dark background for pause screen
        font = pygame.font.Font(None, 36)
        text = font.render('Paused - Press P to Resume', True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 300))
        self.screen.blit(text, text_rect)
        pygame.display.flip()  # Update the full display Surface to the screen

    def get_random_position(self):
        x = random.randrange(1, SCREEN_WIDTH // CELL_SIZE) * CELL_SIZE
        y = random.randrange(1, SCREEN_HEIGHT // CELL_SIZE) * CELL_SIZE
        return [x, y]

    def update_snake(self):
        # Updates the snake's direction based on user input
        if self.direction == 'RIGHT':
            self.snake_position[0] += CELL_SIZE
        elif self.direction == 'LEFT':
            self.snake_position[0] -= CELL_SIZE
        elif self.direction == 'UP':
            self.snake_position[1] -= CELL_SIZE
        elif self.direction == 'DOWN':
            self.snake_position[1] += CELL_SIZE

        self.snake_body.insert(0, list(self.snake_position))

        if self.snake_position == self.fruit_position:
            self.score += SCORE_PER_FRUIT
            if self.score % LEVEL_UP_SCORE == 0:
                self.speed += SPEED_INCREMENT
                self.level += 1
            self.fruit_position = self.get_random_position()
        else:
            self.snake_body.pop()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.close_game()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.paused = not self.paused
                        if self.paused:
                            self.show_pause_screen()
                            save_game_state(self.cursor, self.user_id, self.score, self.level)
                            print("Game paused and state saved.")
                            self.wait_for_unpause()
                        else: 
                            print("Game resumed")
                    else:
                        if not self.paused:
                            self.change_direction(event.key)


            if not self.paused:
                self.update_snake()
                self.render()
            
            self.clock.tick(FRAME_RATE)

    def wait_for_unpause(self):
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = False  # Exit the pause loop

        # We still need to update the display to show the pause screen,
        # otherwise it may appear only briefly.
        pygame.display.update()
        self.clock.tick(15)  # Reduce the frequency of updates while paused
    
    def change_direction(self, key):
        direction_map = {
            pygame.K_UP: 'UP',
            pygame.K_DOWN: 'DOWN',
            pygame.K_LEFT: 'LEFT',
            pygame.K_RIGHT: 'RIGHT'
        }
        if key in direction_map:
            proposed_direction = direction_map[key]
            allowed_directions = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
            if proposed_direction != allowed_directions.get(self.direction):
                self.direction = proposed_direction

    def render(self):
        self.screen.fill(BACKGROUND_COLOR)
        for pos in self.snake_body:
            pygame.draw.rect(self.screen, SNAKE_COLOR, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self.screen, FRUIT_COLOR, pygame.Rect(self.fruit_position[0], self.fruit_position[1], CELL_SIZE, CELL_SIZE))
        show_text(self.screen, f'Score: {self.score}', (50, 10))
        show_text(self.screen, f'Level: {self.level}', (SCREEN_WIDTH - 100, 10))

        # if self.check_game_over():
        #     handle_game_over(self.screen, self.score)
        #     self.reset_game()

        pygame.display.update()
        self.clock.tick(self.speed)

    def check_game_over(self):
        if (self.snake_position[0] < 0 or self.snake_position[0] >= SCREEN_WIDTH or
           self.snake_position[1] < 0 or self.snake_position[1] >= SCREEN_HEIGHT or
           check_collision(self.snake_position, self.snake_body[1:])):
            return True
        return False

    def close_game(self):
        self.cursor.close()
        self.connection.close()
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    username = input("Enter your username: ")
    connection = connect_db()
    cursor = connection.cursor()
    user_id = get_or_create_user(cursor, username)
    cursor.close()
    connection.close()
    
    game = SnakeGame(user_id)
    game.run()
