#!/usr/bin/env python3
import argparse
import serial
import time
from time import sleep
import datetime
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('port')
parser.add_argument('--rows', type=int, default=5)
parser.add_argument('--cols', type=int, default=6)
args = parser.parse_args()

def send(msg, duration=0):
    now = datetime.datetime.now()
    # print(f'[{now}] {msg}')
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')

def leap():
    send("Button HOME", 0.1) # Home
    sleep(0.5)

    send("LY MAX", 0.05)
    sleep(0.05)

    send("LX MAX", 0.05)
    sleep(0.05)

    send("LX MAX", 0.05)
    sleep(0.05)

    send("LX MAX", 0.05)
    sleep(0.05)

    send("LX MAX", 0.05)
    sleep(0.05)

    send("Button A", 0.1) # 設定
    sleep(0.05)

    send("LY MAX", 2.4)
    send("Button A", 0.05) # 本体設定
    sleep(0.05)

    send("LY MAX", 0.05)
    sleep(0.05)

    send("LY MAX", 0.05)
    sleep(0.05)

    send("LY MAX", 0.05)
    sleep(0.05)

    send("LY MAX", 0.05)
    sleep(0.05)

    send("Button A", 0.05) # 日付と時刻選択
    sleep(0.2)

    send("LY MAX", 0.05)
    sleep(0.05)

    send("LY MAX", 0.05)
    sleep(0.05)

    count = 0 # count initialize

    send("Button A", 0.06) # 現在の日付と時刻
    sleep(0.1)


    send("Button A", 0.06)
    sleep(0.05)

    send("Button A", 0.06)
    sleep(0.05)

    send("LY MIN", 0.06) # 日付を１日進める
    sleep(0.1)

    send("Button A", 0.06)
    sleep(0.05)

    send("Button A", 0.06)
    sleep(0.05)

    send("Button A", 0.06)
    sleep(0.05)

    send("Button A", 0.06) # 日付OK
    sleep(0.1)

    send("Button HOME", 0.05)
    sleep(1)

    send("Button A", 0.05)
    sleep(0.5)

def oneDay():
    send("Button A", 0.1) # みんなで挑戦
    sleep(3)

    leap()

    send("Button B", 0.1) # やめる
    sleep(1)

    send("Button A", 0.1) # はい
    sleep(4.5)

    send("Button A", 0.1) # 巣にはなしかける
    sleep(1)

    send("Button A", 0.1) # あふれでている
    sleep(0.7)

    send("Button A", 0.1) # 2000W手に入れた
    sleep(0.7)

def threeDays():
    send("Button B", 0.1) # おまじない
    sleep(0.1)

    send("Button A", 0.1) # ゲーム起動
    sleep(15)

    send("Button A", 0.1) # タイトルA
    sleep(8)

    send("Button A", 0.1) # 巣にはなしかける
    sleep(1)

    send("Button A", 0.1) # あふれでている
    sleep(0.7)

    send("Button A", 0.1) # 200oW手に入れた
    sleep(0.7)

    for i in tqdm(range(3)):
        oneDay()

ser = serial.Serial(args.port, 9600)

try:
    send("Button HOME", 0.1)
    sleep(1)

    send("Button X", 0.1)
    sleep(0.8)

    send("Button A", 0.1)
    sleep(3)

    send("LY MAX", 0.1)
    sleep(0.05)

    send("LX MAX", 0.1)
    sleep(0.05)

    send("LX MAX", 0.1)
    sleep(0.05)

    send("LX MAX", 0.1)
    sleep(0.05)

    send("LX MAX", 0.1)
    sleep(0.05)

    send("Button A", 0.1) # 設定
    sleep(0.1)

    send("LY MAX", 2.5)
    send("Button A", 0.1) # 本体設定
    sleep(0.1)

    send("LY MAX", 0.1)
    sleep(0.05)

    send("LY MAX", 0.1)
    sleep(0.05)

    send("LY MAX", 0.1)
    sleep(0.05)

    send("LY MAX", 0.1)
    sleep(0.05)

    send("Button A", 0.1) # 日付と時刻選択
    sleep(0.2)

    send("LY MAX", 0.1)
    sleep(0.05)

    send("LY MAX", 0.1)
    sleep(0.05)

    count = 0 # count initialize

    send("Button A", 0.1) # 現在の日付と時刻
    sleep(0.1)


    send("Button A", 0.1)
    sleep(0.05)

    send("Button A", 0.1)
    sleep(0.05)

    send("LY MAX", 0.1)
    sleep(0.1)

    send("LY MAX", 0.1)
    sleep(0.1)

    send("LY MAX", 0.1)
    sleep(0.1)

    send("Button A", 0.1)
    sleep(0.05)

    send("Button A", 0.1)
    sleep(0.05)

    send("Button A", 0.1)
    sleep(0.05)

    send("Button A", 0.1) # 日付OK
    sleep(0.1)

    send("Button HOME", 0.1)
    sleep(0.8)

    threeDays()

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()