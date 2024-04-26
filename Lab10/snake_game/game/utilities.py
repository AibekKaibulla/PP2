import pygame
from game.config import FONT_TYPE, FONT_SIZE, TEXT_COLOR

def show_text(screen, text, position, color=TEXT_COLOR, font_size=FONT_SIZE):
    """
    Display text on the screen at a specified position.
    Args:
        screen (pygame.Surface): The pygame display surface to draw on.
        text (str): The text to be displayed.
        position (tuple): A tuple (x, y) representing the position on the screen.
        color (tuple): RGB tuple for the font color.
        font_size (int): The font size.
    """
    font = pygame.font.SysFont(FONT_TYPE, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = position
    screen.blit(text_surface, text_rect)

def check_collision(position, list_of_positions):
    """
    Check if the specified position collides with any positions in a list.
    Args:
        position (list): A list or tuple representing the position to check.
        list_of_positions (list of lists/tuples): A list of positions to check against.
    Returns:
        bool: True if a collision is detected, otherwise False.
    """
    return position in list_of_positions

def handle_game_over(screen, score):
    """
    Handle game over scenario.
    Args:
        screen (pygame.Surface): The pygame display surface to draw on.
        score (int): The final score of the game.
    """
    from game.config import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_OVER_MSG
    show_text(screen, GAME_OVER_MSG + str(score), (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4), color=(255, 0, 0), font_size=50)
    pygame.display.flip()
    pygame.time.wait(2000)  # Wait 2 seconds before continuing
