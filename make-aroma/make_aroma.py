# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO


class MakeAroma():

    def __init__(self):
        # GPIO定義
        self.fan1_pin=15
        self.fan2_pin=18
        self.fan3_pin=20
        self.fan4_pin=26
        self.fan5_pin=12
        self.fan6_pin=16

        # GPIO初期化
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.fan1_pin, GPIO.OUT)
        GPIO.setup(self.fan2_pin, GPIO.OUT)
        GPIO.setup(self.fan3_pin, GPIO.OUT)
        GPIO.setup(self.fan4_pin, GPIO.OUT)
        GPIO.setup(self.fan5_pin, GPIO.OUT)
        GPIO.setup(self.fan6_pin, GPIO.OUT)


    def fan_alloff(self):
        GPIO.output(self.fan1_pin,GPIO.LOW)
        GPIO.output(self.fan2_pin,GPIO.LOW)
        GPIO.output(self.fan3_pin,GPIO.LOW)
        GPIO.output(self.fan4_pin,GPIO.LOW)
        GPIO.output(self.fan5_pin,GPIO.LOW)
        GPIO.output(self.fan6_pin,GPIO.LOW)


    def fan1_on(self):
        GPIO.output(self.fan1_pin,GPIO.HIGH)
        GPIO.output(self.fan2_pin,GPIO.LOW)
        GPIO.output(self.fan3_pin,GPIO.LOW)
        GPIO.output(self.fan4_pin,GPIO.LOW)
        GPIO.output(self.fan5_pin,GPIO.LOW)
        GPIO.output(self.fan6_pin,GPIO.LOW)


    def fan2_on(self):
        GPIO.output(self.fan1_pin,GPIO.LOW)
        GPIO.output(self.fan2_pin,GPIO.HIGH)
        GPIO.output(self.fan3_pin,GPIO.LOW)
        GPIO.output(self.fan4_pin,GPIO.LOW)
        GPIO.output(self.fan5_pin,GPIO.LOW)
        GPIO.output(self.fan6_pin,GPIO.LOW)


    def fan3_on(self):
        GPIO.output(self.fan1_pin,GPIO.LOW)
        GPIO.output(self.fan2_pin,GPIO.LOW)
        GPIO.output(self.fan3_pin,GPIO.HIGH)
        GPIO.output(self.fan4_pin,GPIO.LOW)
        GPIO.output(self.fan5_pin,GPIO.LOW)
        GPIO.output(self.fan6_pin,GPIO.LOW)


    def fan4_on(self):
        GPIO.output(self.fan1_pin,GPIO.LOW)
        GPIO.output(self.fan2_pin,GPIO.LOW)
        GPIO.output(self.fan3_pin,GPIO.LOW)
        GPIO.output(self.fan4_pin,GPIO.HIGH)
        GPIO.output(self.fan5_pin,GPIO.LOW)
        GPIO.output(self.fan6_pin,GPIO.LOW)


    def fan5_on(self):
        GPIO.output(self.fan1_pin,GPIO.LOW)
        GPIO.output(self.fan2_pin,GPIO.LOW)
        GPIO.output(self.fan3_pin,GPIO.LOW)
        GPIO.output(self.fan4_pin,GPIO.LOW)
        GPIO.output(self.fan5_pin,GPIO.HIGH)
        GPIO.output(self.fan6_pin,GPIO.LOW)


    def fan6_on(self):
        GPIO.output(self.fan1_pin,GPIO.LOW)
        GPIO.output(self.fan2_pin,GPIO.LOW)
        GPIO.output(self.fan3_pin,GPIO.LOW)
        GPIO.output(self.fan4_pin,GPIO.LOW)
        GPIO.output(self.fan5_pin,GPIO.LOW)
        GPIO.output(self.fan6_pin,GPIO.HIGH)
