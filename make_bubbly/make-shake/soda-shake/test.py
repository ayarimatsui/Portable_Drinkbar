# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import threading
import numpy as np

#配列データの読み込み

data=np.load(file="soda-array.npy",allow_pickle=True,fix_imports=True,encoding="ASCII")

data=np.power(data,2)

data=360*data/np.max(data)

data=90*data[data<=50]/50

# GPIO定義
bubbly_pin=27

'''on_off=0

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
#th.start()'''

# GPIO初期化
GPIO.setmode(GPIO.BCM)
GPIO.setup(bubbly_pin, GPIO.OUT)
shake=GPIO.PWM(bubbly_pin,100)
shake.start(0)

for i in range(0,len(data),100):
    #print(data[i])
    shake.ChangeDutyCycle(data[i])
    time.sleep(0.01)
    
shake.stop()
GPIO.cleanup()
    


'''try:
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
   
th.join()'''