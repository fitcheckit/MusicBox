import pygame

pygame.mixer.init()

sound_file = "bonk.mp3"
pygame.mixer.music.load(sound_file)


pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
    continue 

pygame.quit()