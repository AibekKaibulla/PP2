import pygame
import sys

def init_pygame():
    pygame.init()
    return pygame.display.set_mode((600, 600)), pygame.Surface((600, 600))

# Handle all pygame events, such as key presses and mouse actions
def handle_events(color, flags):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
            # exit the program
        if event.type == pygame.KEYDOWN: # If a key is pressed down
            color, flags = handle_keydown(event, color, flags) # Handle key presses
        if event.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION]: # Mouse button or motion events
            flags = handle_mouse(event, flags) # Handle mouse events
    return color, flags

# Processes keydown events to change color or toggle drawing modes
def handle_keydown(event, color, flags):
    match event.key:
        case pygame.K_1: 
            color = (0, 0, 0) # Black
        case pygame.K_2:
            color = (255, 0, 0) # Red
        case pygame.K_3: 
            color = (0, 0, 255) # Blue
        case pygame.K_4: 
            color = (255, 255, 0) # Yellow
        case pygame.K_5: 
            color = (124, 252, 0) # Green
        case pygame.K_q:
            flags.update({'drawRect': True, 'drawCircle': False, 'eraser': False}) # Enable rectangle drawing mode
        case pygame.K_w:
            flags.update({'drawRect': False, 'drawCircle': True, 'eraser': False}) # Enable circle drawing mode
        case pygame.K_e:
            flags.update({'drawRect': False, 'drawCircle': False, 'eraser': True}) # Enable eraser mode
        case _:
            pass
    return color, flags

# Handles mouse events for drawing and erasing
def handle_mouse(event, flags):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # If left mouse button is pressed
        flags.update({'isMouseDown': True, 'X': event.pos[0], 'Y': event.pos[1], 'cur_X': event.pos[0], 'cur_Y': event.pos[1]})
    elif event.type == pygame.MOUSEBUTTONUP: # If mouse button is released
        flags.update({'isMouseDown': False})
        layer.blit(screen, (0, 0)) # Copy the screen to the layer to save the current drawing state
    elif event.type == pygame.MOUSEMOTION and flags['isMouseDown']: # If mouse is moving while the button is pressed
        flags.update({'cur_X': event.pos[0], 'cur_Y': event.pos[1]})
    return flags

# Draws shapes on the screen based on the current flags and mouse position
def draw_shapes(screen, layer, color, flags):
    if flags['isMouseDown'] and all(flags[k] != -1 for k in ['X', 'Y', 'cur_X', 'cur_Y']):
        if flags['drawRect']: # If rectangle drawing mode is enabled
            screen.blit(layer, (0, 0)) 
            rect = calculate_rect(flags['X'], flags['Y'], flags['cur_X'], flags['cur_Y'])
            pygame.draw.rect(screen, color, rect, 1) # Draw rectangle
        elif flags['drawCircle']: # If circle drawing mode is enabled
            screen.blit(layer, (0, 0))
            rect = calculate_rect(flags['X'], flags['Y'], flags['cur_X'], flags['cur_Y'])
            pygame.draw.ellipse(screen, color, rect, 1) # Draw ellipse
        if flags['eraser'] and pygame.mouse.get_pressed()[0]: # If eraser mode is enabled and mouse is pressed
            pygame.draw.circle(screen, (255, 255, 255), pygame.mouse.get_pos(), 25) # Erase by drawing a white circle
            
# Calculate the rectangle for drawing based on starting and current mouse positions
def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def main():
    global screen, layer
    screen, layer = init_pygame()
    screen.fill((255, 255, 255))
    layer.fill((255, 255, 255))
    color = (0, 0, 0)
    flags = {'isMouseDown': False, 'drawRect': True, 'drawCircle': False, 'eraser': False, 'X': -1, 'Y': -1, 'cur_X': -1, 'cur_Y': -1}
    clock = pygame.time.Clock()

    while True:
        color, flags = handle_events(color, flags)
        draw_shapes(screen, layer, color, flags)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
