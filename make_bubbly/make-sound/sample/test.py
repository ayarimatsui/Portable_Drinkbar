#from mutagen.mp3 import MP3 as mp3
import pygame.mixer
import time

filename = '../sound/soda-open.ogg'
pygame.init()
soda=pygame.mixer.Sound(filename)
soda.set_volume(1.0)
soda.play()
time.sleep(1.5)