import pygame
import os

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('music player')

music_files = [f for f in os.listdir('music') if f.endswith('.mp3')]
current_track = 0

def play_new_track():
    pygame.mixer.music.load(os.path.join('music', music_files[current_track]))
    pygame.mixer.music.play()

if music_files:
    play_new_track()


# SPACE for play/pause, 'S' for stop, 'N' for next, 'B' for previous
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Play/Pause toggle
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:  # Stop
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:  # Next
                current_track = (current_track + 1) % len(music_files)
                play_new_track()
            elif event.key == pygame.K_b:  # Previous
                current_track = (current_track - 1) % len(music_files)
                play_new_track()

pygame.quit()
