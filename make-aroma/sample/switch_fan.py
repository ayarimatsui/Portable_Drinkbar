# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import threading

# GPIO定義
fan1_pin=14
fan2_pin=15
fan3_pin=18
fan4_pin=23

# すべてのファンがoffのとき0、1~4のときはその番号のファンが回る
switch=0

# 別スレッドを立てて入力を取得
print("0 -> off all fans")
print("1 -> turn on fan1")
print("2 -> turn on fan2")
print("3 -> turn on fan3")
print("4 -> turn on fan4")

def wait_input():
    global switch
    key=input()
    if key=="0":
        switch=0
    elif key=="1":
        switch=1
    elif key=="2":
        switch=2
    elif key=="3":
        switch=3
    elif key=="4":
        switch=4
    #print("on_off = "+str(on_off))

#th = threading.Thread(target=wait_input)
#th.start()

# GPIO初期化
GPIO.setmode(GPIO.BCM)
GPIO.setup(fan1_pin, GPIO.OUT)
GPIO.setup(fan2_pin, GPIO.OUT)
GPIO.setup(fan3_pin, GPIO.OUT)
GPIO.setup(fan4_pin, GPIO.OUT)

try:
    while True:
        th = threading.Thread(target=wait_input)
        th.start()
        if switch==0:
            GPIO.output(fan1_pin,GPIO.LOW)
            GPIO.output(fan2_pin,GPIO.LOW)
            GPIO.output(fan3_pin,GPIO.LOW)
            GPIO.output(fan4_pin,GPIO.LOW)
        elif switch==1:
            GPIO.output(fan1_pin,GPIO.HIGH)
            GPIO.output(fan2_pin,GPIO.LOW)
            GPIO.output(fan3_pin,GPIO.LOW)
            GPIO.output(fan4_pin,GPIO.LOW)
        elif switch==2:
            GPIO.output(fan1_pin,GPIO.LOW)
            GPIO.output(fan2_pin,GPIO.HIGH)
            GPIO.output(fan3_pin,GPIO.LOW)
            GPIO.output(fan4_pin,GPIO.LOW)
        elif switch==3:
            GPIO.output(fan1_pin,GPIO.LOW)
            GPIO.output(fan2_pin,GPIO.LOW)
            GPIO.output(fan3_pin,GPIO.HIGH)
            GPIO.output(fan4_pin,GPIO.LOW)
        elif switch==4:
            GPIO.output(fan1_pin,GPIO.LOW)
            GPIO.output(fan2_pin,GPIO.LOW)
            GPIO.output(fan3_pin,GPIO.LOW)
            GPIO.output(fan4_pin,GPIO.HIGH)
        time.sleep(0.3)

except KeyboardInterrupt:
    pass

finally:
   print("clean up") 
   GPIO.cleanup()
   
th.join()