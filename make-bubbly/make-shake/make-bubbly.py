# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import threading

# GPIO定義
bubbly_pin=27

on_off=0

# 別スレッドを立てて入力を取得
print("1 -> on")
print("0 -> off")


def wait_input():
    global on_off
    global restart_th
    key=input()
    if key=="1":
        on_off=1
        restart_th=1
    elif key=="0":
        on_off=0
    #print("on_off = "+str(on_off))

#th = threading.Thread(target=wait_input)
#th.start()

# GPIO初期化
GPIO.setmode(GPIO.BCM)
GPIO.setup(bubbly_pin, GPIO.OUT)

try:
    while True:
        th = threading.Thread(target=wait_input)
        th.start()
        if on_off==1:
            GPIO.output(bubbly_pin,GPIO.HIGH)
        else:
            GPIO.output(bubbly_pin,GPIO.LOW)
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
   print("clean up") 
   GPIO.cleanup()
   
th.join()