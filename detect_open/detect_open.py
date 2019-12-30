import RPi.GPIO as GPIO

class DetectOpen():
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_UP)
        self.sw_status=0
        
    def get_sw_status(self):
        self.sw_status=GPIO.input(17)
        return self.sw_status