#!/usr/bin/env python3
import argparse
import serial
import time
from time import sleep
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('port')
parser.add_argument('--days', type=int, default=30)
args = parser.parse_args()

def send(msg, duration=0):
    now = datetime.datetime.now()
    print(f'[{now}] {msg}')
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')

def oneDay():
    send("Button A", 0.1) # 現在の日付と時刻
    sleep(0.1)

    send("LX MIN", 0.05)
    sleep(0.05)

    send("LX MIN", 0.05)
    sleep(0.05)

    send("LX MIN", 0.05)
    sleep(0.05)

    send("LY MIN", 0.1) # 日付を１日進める
    sleep(0.1)

    send("Button A", 0.05)
    sleep(0.05)

    send("Button A", 0.05)
    sleep(0.05)

    send("Button A", 0.05)
    sleep(0.05)

    send("Button A", 0.1) # 日付OK
    sleep(0.1)


free_time = 18

ser = serial.Serial(args.port, 9600)

try:
    send("Button B", 0.1)
    send("Button B", 0.1)
    send("Button B", 0.1) # Initialize

    send("Button HOME", 0.1) # Home
    sleep(0.5)

    send("LY MAX", 0.1)
    sleep(0.1)

    send("LX MAX", 0.1)
    sleep(0.1)

    send("LX MAX", 0.1)
    sleep(0.1)

    send("LX MAX", 0.1)
    sleep(0.1)

    send("LX MAX", 0.1)
    sleep(0.1)

    send("Button A", 0.1) # 設定
    sleep(0.1)

    send("LY MAX", 2.5)
    send("Button A", 0.1) # 本体設定
    sleep(0.1)

    send("LY MAX", 0.1)
    sleep(0.1)

    send("LY MAX", 0.1)
    sleep(0.1)

    send("LY MAX", 0.1)
    sleep(0.1)

    send("LY MAX", 0.1)
    sleep(0.1)

    send("Button A", 0.1) # 日付と時刻選択
    sleep(0.2)

    send("LY MAX", 0.1)
    sleep(0.1)

    send("LY MAX", 0.1)
    sleep(0.1)

    count = 0 # count initialize

    send("Button A", 0.1) # 現在の日付と時刻
    sleep(0.1)


    send("Button A", 0.1)
    sleep(0.1)

    send("Button A", 0.1)
    sleep(0.1)

    send("LY MIN", 0.1) # 日付を１日進める
    sleep(0.1)

    send("Button A", 0.1)
    sleep(0.1)

    send("Button A", 0.1)
    sleep(0.1)

    send("Button A", 0.1)
    sleep(0.1)

    send("Button A", 0.1) # 日付OK
    sleep(0.1)

    count += 1

    while True:
        if count == args.days:
            break
        if count % 30 == 0:
            oneDay() # 31日になったら１日進めて日付を１日に戻す

        oneDay()
        count += 1

    send("Button HOME", 0.1)
    sleep(1)
    send("Button A", 0.1)
    sleep(0.5)

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
