#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import string
import ipget
import RPi.GPIO as GPIO
import time
from neopixel import *
import argparse
import pygame
import smbus
import math
import threading
from make-color.make-color import MakeColor  #GPIO.setmode()共通でするべき？？
from make-bubbly.make-bubbly import MakeBubbly
from make-aroma.make-aroma import MakeAroma
from detect_shake.detect-shake import DetectShake
from detect_open.detect-open import DetectOpen

# 音声入力で味を切り替え
switch=0
pre_switch=0

host = "127.0.0.1"  # Raspberry PiのIPアドレス
port = 10500         # juliusの待ち受けポート

# パソコンからTCP/IPで、自分PCのjuliusサーバに接続
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))


if __name__=="__main__":
    try:
        switch=0
        pre_switch=0

        MakeColor.initialize()

        print("味は以下の６種類です")
        print("りんごジュース・紅茶・コーラ・オレンジジュース・ぶどうジュース・メロンソーダ")

        while True:
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
                if strTemp=="リンゴジュース":
                    switch=1
                    print("リンゴジュース")
                elif strTemp=="紅茶":
                    switch=2
                    print("紅茶")
                elif strTemp=="コーラ":
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
                    print("メロンソーダ")
                    
                    
            if switch==0:
                MakeColor.all_off() #全てオフ
                MakeAroma.fan_alloff()
                MakeBubbly.shake_off()
                DetectOpen.get_sw_status() #フタが空いてるかどうかを調べる
                pre_sw_status=DetectOpen.sw_status
                
            elif switch==1: #リンゴジュース
                if pre_switch!=switch: #新しくリンゴジュースが指定された時
                    MakeColor.apple_juice()
                else:                   #リンゴジュースのままの時
                    MakeColor.stay_the_same()
                DetectOpen.get_sw_status() #フタが空いてるかどうかを調べる
                pre_sw_status=DetectOpen.sw_status
                if DetectOpen.sw_status==1: #フタが空いている時
                    MakeAroma.fan1_on() #ファンを回す
                else:
                    MakeAroma.fan_alloff()
                    
            elif switch==2: #紅茶
                if pre_switch!=switch: #新しく紅茶が指定された時
                    MakeColor.black_tea()
                else:                   #紅茶のままの時
                    MakeColor.stay_the_same()
                DetectOpen.get_sw_status() #フタが空いてるかどうかを調べる
                pre_sw_status=DetectOpen.sw_status
                if DetectOpen.sw_status==1: #フタが空いている時
                    MakeAroma.fan2_on() #ファンを回す
                else:
                    MakeAroma.fan_alloff()
                    
            elif switch==3: #コーラ
                if pre_switch!=switch: #新しくコーラが指定された時
                    MakeColor.coke()
                else:                   #コーラのままの時
                    MakeColor.stay_the_same()
                DetectOpen.get_sw_status() #フタが空いてるかどうかを調べる
                if DetectOpen.sw_status==1: #フタが空いている時
                    MakeAroma.fan3_on() #ファンを回す
                    if pre_sw_status!=sw_status:
                        MakeBubbly.sound_play()
                    else:
                        MakeBubbly.shake_on()
                else:
                    MakeAroma.fan_alloff()
                    MakeBubbly.shake_off()
                pre_sw_status=DetectOpen.sw_status
                
            elif switch==4: #オレンジジュース
                if pre_switch!=switch: #新しくオレンジジュースが指定された時
                    MakeColor.orange_juice()
                else:                   #オレンジジュースのままの時
                    MakeColor.stay_the_same()
                DetectOpen.get_sw_status() #フタが空いてるかどうかを調べる
                pre_sw_status=DetectOpen.sw_status
                if DetectOpen.sw_status==1: #フタが空いている時
                    MakeAroma.fan4_on() #ファンを回す
                else:
                    MakeAroma.fan_alloff()
                    
            elif switch==5: #ぶどうジュース
                if pre_switch!=switch: #新しくぶどうジュースが指定された時
                    MakeColor.grape_juice()
                else:                   #ぶどうジュースのままの時
                    MakeColor.stay_the_same()
                DetectOpen.get_sw_status() #フタが空いてるかどうかを調べる
                pre_sw_status=DetectOpen.sw_status
                if DetectOpen.sw_status==1: #フタが空いている時
                    MakeAroma.fan5_on() #ファンを回す
                else:
                    MakeAroma.fan_alloff()
                    
            elif switch==6: #メロンソーダ
                if pre_switch!=switch: #新しくメロンソーダが指定された時
                    MakeColor.coke()
                else:                   #メロンソーダのままの時
                    MakeColor.stay_the_same()
                DetectOpen.get_sw_status() #フタが空いてるかどうかを調べる
                if DetectOpen.sw_status==1: #フタが空いている時
                    MakeAroma.fan6_on() #ファンを回す
                    if pre_sw_status!=sw_status:
                        MakeBubbly.sound_play()
                    else:
                        MakeBubbly.shake_on()
                else:
                    MakeAroma.fan_alloff()
                    MakeBubbly.shake_off()
                pre_sw_status=DetectOpen.sw_status
                
            else:
                MakeColor.all_off() #全てオフ
                MakeAroma.fan_alloff()
                MakeBubbly.shake_off()
                DetectOpen.get_sw_status() #フタが空いてるかどうかを調べる
                pre_sw_status=DetectOpen.sw_status
                
            pre_switch=switch
            time.sleep(0.3)

    except KeyboardInterrupt:
        pass

    finally:
       print("clean up")
       GPIO.cleanup()
