#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import string
import sys
sys.path.append('/home/pi/.local/lib/python2.7/site-packages')
import ipget
import RPi.GPIO as GPIO
import time
from neopixel import *
import argparse
import pygame.mixer
import smbus
import math
import threading
import numpy as np
from make_color.make_color import MakeColor
from make_aroma.make_aroma import MakeAroma
from detect_shake.detect_shake import DetectShake
from detect_open.detect_open import DetectOpen


# 音声入力で味を切り替え
switch=0
pre_switch=0

host = "127.0.0.1"  # Raspberry PiのIPアドレス
port = 10500         # juliusの待ち受けポート

# パソコンからTCP/IPで、自分PCのjuliusサーバに接続
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))


#音声入力スレッドを終わらせるためのflag
end_flag=0

def wait_input():
    global switch
    global end_flag
    data = ""
    while end_flag==0:
        # "/RECOGOUT"を受信するまで、一回分の音声データを全部読み込む。
        while (string.find(data, "\n.") == -1):
            data = data + sock.recv(1024)

        # 音声XMLデータから、<WORD>を抽出して音声テキスト文に連結する。
        strTemp = ""
        for line in data.split('\n'):
            index = line.find('WORD="')

            if index != -1:
                line = line[index + 6:line.find('"', index + 6)]
                if line != "[s]":
                    strTemp = strTemp + line

        if strTemp != "":
            '''if strTemp=="リンゴジュース":
                switch=1
                print("リンゴジュース")
                break'''
            if strTemp=="紅茶":
                switch=2
                print("紅茶")
            '''elif strTemp=="コーラ":
                switch=3
                print("コーラ")
            elif strTemp=="オレンジジュース":
                switch=4
                print("オレンジジュース")
            elif strTemp=="ぶどうジュース":
                switch=5
                print("ぶどうジュース")
            elif strTemp=="メロンソーダ":
                switch=6
                print("メロンソーダ")'''
                  
        data = ""
 
 
### 振動モーター制御のスレッド
#  振動させるかどうかのフラグ
shake_on=0

#  振動モーター制御のスレッドを終わらせるためのフラグ
end_flag2=0

def make_shake():
    global shake_on
    global end_flag2

    #配列データの読み込み

    data=np.load(file="make_bubbly/make-shake/soda-shake/soda-array.npy",allow_pickle=True,fix_imports=True,encoding="ASCII")

    data=np.power(data,2)

    data=360*data/np.max(data)

    data=90*data[data<=50]/50

    # GPIO定義
    bubbly_pin=27

    # GPIO初期化
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(bubbly_pin, GPIO.OUT)
    shake=GPIO.PWM(bubbly_pin,100)
    shake.start(0)
    
    while end_flag2==0:
        if shake_on==0:
            while shake_on==0:
                for i in range(100):
                    shake.ChangeDutyCycle(0)
                    time.sleep(0.01)
        else:
            while shake_on==1:
                for i in range(0,len(data),100):
                    if shake_on==0:
                        break
                    shake.ChangeDutyCycle(data[i])
                    time.sleep(0.01)
            
    shake.stop()
        
        

if __name__=="__main__":
    MakeColor=MakeColor()
    #MakeBubbly=MakeBubbly()
    MakeAroma=MakeAroma()
    DetectShake=DetectShake()
    DetectOpen=DetectOpen()
    #炭酸の音の設定
    filename = 'make_bubbly/make-sound/sound/soda-open.ogg'
    pygame.init()
    pygame.mixer.init()
    soda=pygame.mixer.Sound(filename)
    #soda.set_volume(1.0)
    try:
        switch=0
        pre_switch=0
        shake_on=0

        MakeColor.initialize()
        MakeColor.all_off()

        print("「紅茶」というと、紅茶になります")
        #print("味は以下の６種類です")
        #print("りんごジュース・紅茶・コーラ・オレンジジュース・ぶどうジュース・メロンソーダ")
        
        th=threading.Thread(target=wait_input)
        th.setDaemon(True)
        th.start()
        
        th_shake=threading.Thread(target=make_shake)
        th_shake.setDaemon(True)
        th_shake.start()
        

        while True:
            #print(switch)
                    
            if switch==0:
                MakeColor.all_off() #全てオフ
                MakeAroma.fan_alloff()
                #MakeBubbly.shake_off()
                sw_status=DetectOpen.get_sw_status() #フタが空いてるかどうかを調べる
                pre_sw_status=sw_status
                
            elif switch==1: #リンゴジュース
                if pre_switch!=switch: #新しくリンゴジュースが指定された時
                    MakeColor.apple_juice()
                else:                   #リンゴジュースのままの時
                    MakeColor.stay_the_same()
                sw_status=DetectOpen.get_sw_status() #フタが空いてるかどうかを調べる
                pre_sw_status=sw_status
                shake_on=0
                if sw_status==1: #フタが空いている時
                    MakeAroma.fan1_on() #ファンを回す
                else:
                    MakeAroma.fan_alloff()
                    
            elif switch==2: #紅茶
                if pre_switch!=switch: #新しく紅茶が指定された時
                    MakeColor.black_tea()
                else:                   #紅茶のままの時
                    MakeColor.stay_the_same()
                sw_status=DetectOpen.get_sw_status() #フタが空いてるかどうかを調べる
                pre_sw_status=sw_status
                shake_on=0
                if sw_status==1: #フタが空いている時
                    MakeAroma.fan2_on() #ファンを回す
                else:
                    MakeAroma.fan_alloff()
                    
            elif switch==3: #コーラ
                if pre_switch!=switch: #新しくコーラが指定された時
                    MakeColor.coke()
                else:                   #コーラのままの時
                    MakeColor.stay_the_same()
                sw_status=DetectOpen.get_sw_status() #フタが空いてるかどうかを調べる
                if sw_status==1: #フタが空いている時
                    MakeAroma.fan3_on() #ファンを回す
                    if pre_sw_status!=sw_status: #フタが空いた瞬間
                        #炭酸飲料のフタを開けたときの音を再生
                        soda.play()
                        time.sleep(1.5)
                        #MakeBubbly.sound_play()
                    else:
                        shake_on=1
                        #MakeBubbly.shake_on()
                else:
                    MakeAroma.fan_alloff()
                    shake_on=0
                    #MakeBubbly.shake_off()
                pre_sw_status=sw_status
                
            elif switch==4: #オレンジジュース
                if pre_switch!=switch: #新しくオレンジジュースが指定された時
                    MakeColor.orange_juice()
                else:                   #オレンジジュースのままの時
                    MakeColor.stay_the_same()
                sw_status=DetectOpen.get_sw_status() #フタが空いてるかどうかを調べる
                pre_sw_status=sw_status
                shake_on=0
                '''if sw_status==1: #フタが空いている時
                    MakeAroma.fan4_on() #ファンを回す
                else:
                    MakeAroma.fan_alloff()'''
                    
            elif switch==5: #ぶどうジュース
                if pre_switch!=switch: #新しくぶどうジュースが指定された時
                    MakeColor.grape_juice()
                else:                   #ぶどうジュースのままの時
                    MakeColor.stay_the_same()
                sw_status=DetectOpen.get_sw_status() #フタが空いてるかどうかを調べる
                pre_sw_status=sw_status
                shake_on=0
                if sw_status==1: #フタが空いている時
                    MakeAroma.fan5_on() #ファンを回す
                else:
                    MakeAroma.fan_alloff()
                    
            elif switch==6: #メロンソーダ
                if pre_switch!=switch: #新しくメロンソーダが指定された時
                    MakeColor.meron_soda()
                else:                   #メロンソーダのままの時
                    MakeColor.stay_the_same()
                sw_status=DetectOpen.get_sw_status() #フタが空いてるかどうかを調べる
                if sw_status==1: #フタが空いている時
                    MakeAroma.fan6_on() #ファンを回す
                    if pre_sw_status!=sw_status:
                        #炭酸飲料のフタを開けたときの音を再生
                        soda.play()
                        time.sleep(1.5)
                        #MakeBubbly.sound_play()
                    else:
                        shake_on=1
                        #MakeBubbly.shake_on()
                else:
                    MakeAroma.fan_alloff()
                    shake_on=0
                    #MakeBubbly.shake_off()
                pre_sw_status=sw_status
                
            else:
                MakeColor.all_off() #全てオフ
                MakeAroma.fan_alloff()
                shake_on=0
                #MakeBubbly.shake_off()
                sw_status=DetectOpen.get_sw_status() #フタが空いてるかどうかを調べる
                pre_sw_status=sw_status
                
            pre_switch=switch
            time.sleep(0.1)
            

    except KeyboardInterrupt:
        pass

    finally:
        end_flag=1
        end_flag2=1
        print("clean up")
        GPIO.cleanup()
       
    th.join()
    print("end")