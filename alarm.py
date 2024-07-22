import sys
import pygame
import time
# File setup for sounds
path = "/home/raspi6/lettercontainer/"

# pygame setup
pygame.mixer.init()
speaker_volume = 1.0 # set volume
pygame.mixer.music.set_volume(speaker_volume)

pygame.mixer.music.load(path + "beep.wav")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True: 
      continue
    


pygame.display.quit()
pygame.quit()
sys.exit()


