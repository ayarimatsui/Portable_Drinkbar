# -*- coding: utf-8 -*-
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

# キー入力で味を切り替え
switch=0
pre_switch=0

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
    elif key=="5":
        switch=5
    elif key=="6":
        switch=6
    print(switch)


if __name__=="__main__":
    try:
        switch=0
        pre_switch=0

        MakeColor.initialize()

        # 別スレッドを立てて入力を取得
        print("0 -> no flavor")
        print("1 -> apple juice")
        print("2 -> black tea")
        print("3 -> coke")
        print("4 -> orange juice")
        print("5 -> grape juice")
        print("6 -> meron soda")

        while True:
            th = threading.Thread(target=wait_input)
            th.start()
            if switch==0:
                MakeColor.all_off() #全てオフ
                MakeAroma.fan_alloff()
                MakeBubbly.shake_off()
                pre_sw_status=0
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
                print("your input is unavailable.")
                print("please enter number following the instraction below.")
                print("0 -> no flavor")
                print("1 -> apple juice")
                print("2 -> black tea")
                print("3 -> coke")
                print("4 -> orange juice")
                print("5 -> grape juice")
                print("6 -> meron soda")
            pre_switch=switch
            time.sleep(0.3)

    except KeyboardInterrupt:
        pass

    finally:
       print("clean up")
       GPIO.cleanup()

    th.join()
