import pygame
import sys
import random

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.cell_size = 10

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()

        # Start a new game
        self.reset_game()

    def get_random_position(self):
        # Generates a random position for the fruit
        x = random.randrange(1, self.screen_width // self.cell_size) * self.cell_size
        y = random.randrange(1, self.screen_height // self.cell_size) * self.cell_size
        return [x, y]

    def reset_game(self):
        # Resets the game by setting all game parameters to their initial state
        self.snake_position = [300, 300]
        self.snake_body = [
            [300, 300], [290, 300], [280, 300], [270, 300]
        ]
        self.fruit_position = self.get_random_position()
        self.fruit_spawn = True
        self.score = 0
        self.speed = 15
        self.level = 1
        self.direction = 'RIGHT'
        self.change_to = self.direction

    def show_text(self, text, position, color=(255, 255, 255), font_size=20):
        # Display text on the screen
        font = pygame.font.SysFont('Verdana', font_size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = position
        self.screen.blit(text_surface, text_rect)

    def check_collision(self, position, list_of_positions):
        # Checks if the given position collides with any positions in a list
        return position in list_of_positions

    def update_snake(self):
        # Updates the snake's position and checks for collisions with the fruit
        if self.direction == 'RIGHT':
            self.snake_position[0] += self.cell_size
        elif self.direction == 'LEFT':
            self.snake_position[0] -= self.cell_size
        elif self.direction == 'UP':
            self.snake_position[1] -= self.cell_size
        elif self.direction == 'DOWN':
            self.snake_position[1] += self.cell_size

        # Insert new position to the beginning of the snake body
        self.snake_body.insert(0, list(self.snake_position))

        # Check if snake has eaten the fruit
        if self.snake_position == self.fruit_position:
            self.score += 5 # Increase the score
            if self.score % 20 == 0: # Every 20 points increase speed and level
                self.speed += 5
                self.level += 1
            self.fruit_spawn = False
        else:
            # Remove the last segment of the snake if no fruit was eaten
            self.snake_body.pop()

    def handle_keys(self):
        # Handles key press events to change snake direction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                key_map = {
                    pygame.K_UP: 'UP', pygame.K_DOWN: 'DOWN',
                    pygame.K_LEFT: 'LEFT', pygame.K_RIGHT: 'RIGHT'
                }
                if event.key in key_map:
                    # Set new direction if it's not directly opposite to current direction
                    self.change_to = key_map[event.key]

    def update_direction(self):
        # Updates the direction of the snake if not directly opposite to current direction
        opposite_directions = [('UP', 'DOWN'), ('LEFT', 'RIGHT')]
        if (self.change_to, self.direction) not in opposite_directions and (self.direction, self.change_to) not in opposite_directions:
            self.direction = self.change_to

    def run(self):
        while True:
            self.handle_keys()
            self.update_direction()
            self.update_snake()
            if not self.fruit_spawn:
                # Generates new fruit position if needed and ensures it doesn't collide with the snake
                self.fruit_position = self.get_random_position()
                if not self.check_collision(self.fruit_position, self.snake_body):
                    self.fruit_spawn = True

            self.screen.fill((0, 0, 0))
            # Draw the snake and the fruit
            for pos in self.snake_body:
                pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], self.cell_size, self.cell_size))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.fruit_position[0], self.fruit_position[1], self.cell_size, self.cell_size))

            # Show the current score and level
            self.show_text(f'Score : {self.score}', (50, 10))
            self.show_text(f'Level: {self.level}', (750, 10))
            
            # Check for game over conditions
            if self.snake_position[0] < 0 or self.snake_position[0] >= self.screen_width or \
               self.snake_position[1] < 0 or self.snake_position[1] >= self.screen_height or \
               self.check_collision(self.snake_position, self.snake_body[1:]):
                self.show_text('Game Over! Your Score is: ' + str(self.score), (self.screen_width // 2, self.screen_height // 4), (255, 0, 0), 50)
                pygame.display.flip()
                pygame.time.wait(2000)
                self.reset_game()

            pygame.display.update()
            self.clock.tick(self.speed)

if __name__ == '__main__':
    game = SnakeGame()
    game.run()
