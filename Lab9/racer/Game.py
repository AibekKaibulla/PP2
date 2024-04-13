# Imports
import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
CASH = 0

# Coin collection sound effect
coin_sound = pygame.mixer.Sound("collectcoin.mp3")

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Background image
background = pygame.image.load("AnimatedStreet.png")

# Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Sprite Groups
enemies = pygame.sprite.Group()
bank = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        # Set the initial position of the enemy at a random location at the top of the screen
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        # Moves the enemy down at the current speed. If it moves off the screen, reset position and increment score
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        # Set the initial position of the player near the bottom center of the screen
        self.rect.center = (160, 520)
       
    def move(self):
        # Moves the player based on key presses (left or right), making sure the player doesn't move off-screen
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  

class Money(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("money12.png")
        self.rect = self.image.get_rect()
        self.weight = random.choice([1, 2, 5]) # Random weight for the coin
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.spawn()

    def spawn(self):
        # Ensure Money does not spawn on an Enemy
        collision = True
        while collision:
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            collision = pygame.sprite.spritecollideany(self, enemies)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.spawn()


# Sprite Instances and Adding to Groups
P1 = Player()
E1 = Enemy()
M1 = Money()
enemies.add(E1)
bank.add(M1)
all_sprites.add(P1, E1, M1)

# Sets up a user event to increase speed periodically 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:
      
    #Cycles through all events occuring + speed increment
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draws the background and updates the display with the score and cash
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    money = font_small.render(str(CASH), True, YELLOW)
    DISPLAYSURF.blit(money, (360, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
    
    # Collect coins and update score based on coin weight
    coins_collected = pygame.sprite.spritecollide(P1, bank, dokill=False)
    for coin in coins_collected:
        CASH += coin.weight  # Increment cash by the coin's weight
        coin_sound.play()
        coin.spawn()  # Respawn the collected coin
    
    
    # Increase enemy speed if a certain number of coins have been collected
    if SCORE // 10 > SPEED - 5:  # Assuming you want the enemy speed to increase for every 10 coins
        SPEED += 1  # Increase speed

    # Ends the game if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)
