# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import pygame.mixer

class MakeBubbly():
    
    def __init__(self):
        # GPIO定義
        self.bubbly_pin=27
        # GPIO初期化
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bubbly_pin, GPIO.OUT)
        filename = '../sound/soda-open.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(filename) 


    def shake_on(self):
        GPIO.output(self.bubbly_pin,GPIO.HIGH)
        
        
    def shake_off(self):
        GPIO.output(self.bubbly_pin,GPIO.LOW)
        
    
    def sound_play(self):
        pygame.mixer.music.play(1)
        time.sleep(1)
        pygame.mixer.music.stop()
