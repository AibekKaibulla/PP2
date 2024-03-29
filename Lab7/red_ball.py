import pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Red Ball")

white = (255, 255, 255)
red = (255, 0, 0)

ball_pos = [width // 2, height // 2]
ball_radius = 25
ball_speed = 20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_pos[1] - ball_speed >= ball_radius:
                ball_pos[1] -= ball_speed
            elif event.key == pygame.K_DOWN and ball_pos[1] + ball_speed <= height - ball_radius:
                ball_pos[1] += ball_speed
            elif event.key == pygame.K_LEFT and ball_pos[0] - ball_speed >= ball_radius:
                ball_pos[0] -= ball_speed
            elif event.key == pygame.K_RIGHT and ball_pos[0] + ball_speed <= width - ball_radius:
                ball_pos[0] += ball_speed

    screen.fill(white)

    pygame.draw.circle(screen, red, ball_pos, ball_radius)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()