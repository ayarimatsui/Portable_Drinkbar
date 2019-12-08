# -*- coding: utf-8 -*-
#実行するときは。sudo python ...
from neopixel import *
import argparse

class MakeColor():

    def __init__(self)
        # LED strip configuration:
        LED_COUNT1     = 24     # Number of LED pixels.
        LED_COUNT2     = 7
        LED_PIN1       = 21      # GPIO pin connected to the pixels (18 uses PWM!).
        LED_PIN2       = 10
        LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
        LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
        LED_BRIGHTNESS = 72     # Set to 0 for darkest and 255 for brightest
        LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
        LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
        
        # Process arguments
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
        args = parser.parse_args()

        # Create NeoPixel object with appropriate configuration.
        self.strip1 = Adafruit_NeoPixel(LED_COUNT1, LED_PIN1, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        self.strip2 = Adafruit_NeoPixel(LED_COUNT2, LED_PIN2, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        # Intialize the library (must be called once before other functions).
        self.strip1.begin()
        self.strip2.begin()


    # Define functions which animate LEDs in various ways.
    def color_appears(self, strip, color, wait_ms=30):
        """Wipe color across display a pixel at a time."""
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
     
     
    def show_color(self, strip, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            strip.show()
 
 
    def wheel(self, pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)


    def rainbowCycle(self, strip, wait_ms=10, iterations=1):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(256*iterations):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
            strip.show()
            time.sleep(wait_ms/1000.0)


    def initialize(self):
        show_color(self.strip2,Color(0,0,0))
        rainbowCycle(self.strip1)
        self.color=Color(0,0,0)


    def apple_juice(self):
        self.color=Color(200, 240, 40)
        color_appears(self.strip1, self.color)  # wipe
        color_appears(self.strip2, self.color)  # wipe
        
        
    def black_tea(self):
        self.color=Color(36, 120, 6)
        color_appears(strip1, self.color)  # wipe
        color_appears(strip2, self.color)  # wipe
        
        
    def coke(self):
        self.color=Color(0, 240, 0)
        color_appears(strip1, self.color)  # wipe
        color_appears(strip2, self.color)  # wipe
        
        
    def coffee(self):
        self.color=Color(45, 80, 18)
        color_appears(strip1, self.color)  # wipe
        color_appears(strip2, self.color)  # wipe
        
        
    def grapefruit_juice(self):
        self.color=Color(60, 160, 21)
        color_appears(strip1, self.color)  # wipe
        color_appears(strip2, self.color)  # wipe
        
        
    def orange_juice(self):
        self.color=Color(70, 255, 0)
        color_appears(strip1, self.color)  # wipe
        color_appears(strip2, self.color)  # wipe


    def grape_juice(self):
        self.color=Color(0, 200, 210)
        color_appears(strip1, self.color)  # wipe
        color_appears(strip2, self.color)  # wipe
        
        
    def meron_soda(self):
        self.color=Color(200, 0, 20)
        color_appears(strip1, self.color)  # wipe
        color_appears(strip2, self.color)  # wipe

    
    def stay_the_same(self):
        show_color(strip1, self.color)
        show_color(strip2, self.color)
        