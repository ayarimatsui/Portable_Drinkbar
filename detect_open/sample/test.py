import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_UP)

sw_status=0

while True:
    try:
        sw_status=GPIO.input(17)
        if sw_status==0:
            print("close")
        else:
            print("open")
            
        time.sleep(0.01)
    except:
        break
    
GPIO.cleanup()