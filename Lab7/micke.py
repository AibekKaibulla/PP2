import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((1400, 900))
clock = pygame.time.Clock()

def blitRotate(surf, image, pos, originPos, angle):
    # calculate the axis aligned bounding box of the rotated image
    w, h = image.get_size()
    box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    # calculate the translation of the pivot 
    pivot = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (pos[0] - image.get_rect().width / 2 + min_box[0] - pivot_move[0], pos[1] - image.get_rect().height / 2 - max_box[1] + pivot_move[1])

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    surf.blit(rotated_image, origin)


clock_face_img = pygame.image.load(r'Lab7\mickeyclock.jpeg')
image1 = pygame.image.load(r'Lab7\minute_hand.png')
image2 = pygame.image.load(r'Lab7\second_hand.png')

w1, h1 = image1.get_size()
w2, h2 = image2.get_size()

done = False

while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    minute_angle = -6 * minutes  # 360 degrees / 60 minutes
    second_angle = -6 * seconds  # Same for seconds

    pos = (screen.get_width()/2, screen.get_height()/2)
    
    clock_face_rect = clock_face_img.get_rect(center=pos)

    screen.fill(0)
    screen.blit(clock_face_img, clock_face_rect)

    blitRotate(screen, image1, pos, (w1/2, h1/2), minute_angle)
    blitRotate(screen, image2, pos, (w2/2, h2/2), second_angle)


    pygame.display.flip()
    
pygame.quit()
