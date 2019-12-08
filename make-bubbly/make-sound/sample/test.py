#from mutagen.mp3 import MP3 as mp3
import pygame.mixer
import time

filename = '../sound/soda-open.mp3'
pygame.mixer.init()
pygame.mixer.music.load(filename) 
pygame.mixer.music.play(1)
time.sleep(1)
pygame.mixer.music.stop()