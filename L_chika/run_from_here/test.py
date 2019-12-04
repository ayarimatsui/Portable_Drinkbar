import threading
import time
from neopixel import *
import argparse

# LED strip configuration:
LED_COUNT1     = 24     # Number of LED pixels.
LED_COUNT2     = 7
LED_PIN1       = 21      # GPIO pin connected to the pixels (18 uses PWM!).
LED_PIN2       = 10
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 72     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53



# Define functions which animate LEDs in various ways.
def color_appears(strip, color, wait_ms=30):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
        
def show_color(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        
def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbowCycle(strip, wait_ms=10, iterations=1):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)
        

print("1 -> apple_juice")
print("2 -> black_tea")
print("3 -> coke")
print("4 -> coffee")
print("5 -> grapefruit_juice")
print("6 -> orange_juice")
print("7 -> wine")

drink=0
pre_drink=0

def wait_input():
    global drink
    key=input()
    drink=int(key)


# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip1 = Adafruit_NeoPixel(LED_COUNT1, LED_PIN1, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip2 = Adafruit_NeoPixel(LED_COUNT2, LED_PIN2, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip1.begin()
    strip2.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')
        
    try:
        print("init")
        show_color(strip2,Color(0,0,0))
        rainbowCycle(strip1)
        color=Color(0,0,0)
        while True:
            th = threading.Thread(target=wait_input)
            th.start()
            if drink!=pre_drink:
                if drink==1:
                    color=Color(200, 240, 40)
                    color_appears(strip1, color)  # wipe
                    color_appears(strip2, color)  # wipe
                elif drink==2:
                    color=Color(36, 120, 6)
                    color_appears(strip1, color)  # wipe
                    color_appears(strip2, color)  # wipe
                elif drink==3:
                    color=Color(0, 240, 0)
                    color_appears(strip1, color)  # wipe
                    color_appears(strip2, color)  # wipe
                elif drink==4:
                    color=Color(45, 80, 18)
                    color_appears(strip1, color)  # wipe
                    color_appears(strip2, color)  # wipe
                elif drink==5:
                    color=Color(60, 160, 21)
                    color_appears(strip1, color)  # wipe
                    color_appears(strip2, color)  # wipe 
                elif drink==6:
                    color=Color(70, 255, 0)
                    color_appears(strip1, color)  # wipe
                    color_appears(strip2, color)  # wipe
                elif drink==7:
                    color=Color(0, 200, 120)
                    color_appears(strip1, color)  # wipe
                    color_appears(strip2, color)  # wipe
            else:
                show_color(strip1, color)
                show_color(strip2, color)
            pre_drink=drink
            time.sleep(0.3)
            

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)

th.join()