# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import pygame

class MakeBubbly():

    def __init__(self):
        '''# GPIO定義
        self.bubbly_pin=27
        # GPIO初期化
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bubbly_pin, GPIO.OUT)'''
        filename = '../sound/soda-open.ogg'
        pygame.init()
        self.soda=pygame.mixer.Sound(filename)


    def shake_on(self):
        GPIO.output(self.bubbly_pin,GPIO.HIGH)


    def shake_off(self):
        GPIO.output(self.bubbly_pin,GPIO.LOW)


    def sound_play(self):
        self.soda.play()
        time.sleep(1.5)

if __name__=="__main__":
    sound=MakeBubbly()
    sound.sound_play()