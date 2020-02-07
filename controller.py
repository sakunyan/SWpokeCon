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

def nDays(n):
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

    for i in tqdm(range(n)):
        oneDay()

def finish(n):
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

    for i in range(n):
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

def fastOneDay():
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

def fastTimeLeap(n):
    bar = tqdm(total=n)

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
    bar.update(1)

    while True:
        if count == n:
            break
        if count % 30 == 0:
            fastOneDay() # 31日になったら１日進めて日付を１日に戻す

        fastOneDay()
        count += 1
        bar.update(1)

    send("Button HOME", 0.1)
    sleep(1)
    send("Button A", 0.1)
    sleep(0.5)

class Controller:
    def __init__(self):
        super().__init__()
        self.today = 1
        self.ser = serial.Serial(args.port, 9600)

    def send(self, msg, duration=0):
        now = datetime.datetime.now()
        # print(f'[{now}] {msg}')
        self.ser.write(f'{msg}\r\n'.encode('utf-8'))
        sleep(duration)
        self.ser.write(b'RELEASE\r\n')

    def leap(self):
        self.send("Button HOME", 0.1) # Home
        sleep(0.5)

        self.send("LY MAX", 0.05)
        sleep(0.05)

        self.send("LX MAX", 0.05)
        sleep(0.05)

        self.send("LX MAX", 0.05)
        sleep(0.05)

        self.send("LX MAX", 0.05)
        sleep(0.05)

        self.send("LX MAX", 0.05)
        sleep(0.05)

        self.send("Button A", 0.1) # 設定
        sleep(0.05)

        self.send("LY MAX", 2.4)
        self.send("Button A", 0.05) # 本体設定
        sleep(0.05)

        self.send("LY MAX", 0.05)
        sleep(0.05)

        self.send("LY MAX", 0.05)
        sleep(0.05)

        self.send("LY MAX", 0.05)
        sleep(0.05)

        self.send("LY MAX", 0.05)
        sleep(0.05)

        self.send("Button A", 0.05) # 日付と時刻選択
        sleep(0.2)

        self.send("LY MAX", 0.05)
        sleep(0.05)

        self.send("LY MAX", 0.05)
        sleep(0.05)

        count = 0 # count initialize

        self.send("Button A", 0.06) # 現在の日付と時刻
        sleep(0.1)


        self.send("Button A", 0.06)
        sleep(0.05)

        self.send("Button A", 0.06)
        sleep(0.05)

        self.send("LY MIN", 0.06) # 日付を１日進める
        sleep(0.1)

        self.send("Button A", 0.06)
        sleep(0.05)

        self.send("Button A", 0.06)
        sleep(0.05)

        self.send("Button A", 0.06)
        sleep(0.05)

        self.send("Button A", 0.06) # 日付OK
        sleep(0.1)

        self.send("Button HOME", 0.05)
        sleep(1)

        self.send("Button A", 0.05)
        sleep(0.5)

    def oneDay(self):
        self.send("Button A", 0.1) # みんなで挑戦
        sleep(3)

        leap()

        self.send("Button B", 0.1) # やめる
        sleep(1)

        self.send("Button A", 0.1) # はい
        sleep(4.5)

        self.send("Button A", 0.1) # 巣にはなしかける
        sleep(1)

        self.send("Button A", 0.1) # あふれでている
        sleep(0.7)

        self.send("Button A", 0.1) # 2000W手に入れた
        sleep(0.7)

    def nDays(self, n):
        self.send("Button A", 0.1) # ゲーム起動
        sleep(15)

        self.send("Button A", 0.1) # タイトルA
        sleep(8)

        self.send("Button A", 0.1) # 巣にはなしかける
        sleep(1)

        self.send("Button A", 0.1) # あふれでている
        sleep(0.7)

        self.send("Button A", 0.1) # 200oW手に入れた
        sleep(0.7)

        for i in tqdm(range(n)):
            self.oneDay()

    def finish(self, n):
        self.send("Button HOME", 0.1)
        sleep(1)

        self.send("Button X", 0.1)
        sleep(0.8)

        self.send("Button A", 0.1)
        sleep(3)

        self.send("LY MAX", 0.1)
        sleep(0.05)

        self.send("LX MAX", 0.1)
        sleep(0.05)

        self.send("LX MAX", 0.1)
        sleep(0.05)

        self.send("LX MAX", 0.1)
        sleep(0.05)

        self.send("LX MAX", 0.1)
        sleep(0.05)

        self.send("Button A", 0.1) # 設定
        sleep(0.1)

        self.send("LY MAX", 2.5)
        self.send("Button A", 0.1) # 本体設定
        sleep(0.1)

        self.send("LY MAX", 0.1)
        sleep(0.05)

        self.send("LY MAX", 0.1)
        sleep(0.05)

        self.send("LY MAX", 0.1)
        sleep(0.05)

        self.send("LY MAX", 0.1)
        sleep(0.05)

        self.send("Button A", 0.1) # 日付と時刻選択
        sleep(0.2)

        self.send("LY MAX", 0.1)
        sleep(0.05)

        self.send("LY MAX", 0.1)
        sleep(0.05)

        count = 0 # count initialize

        self.send("Button A", 0.1) # 現在の日付と時刻
        sleep(0.1)


        self.send("Button A", 0.1)
        sleep(0.05)

        self.send("Button A", 0.1)
        sleep(0.05)

        for i in range(n):
            self.send("LY MAX", 0.1)
            sleep(0.1)

        self.send("Button A", 0.1)
        sleep(0.05)

        self.send("Button A", 0.1)
        sleep(0.05)

        self.send("Button A", 0.1)
        sleep(0.05)

        self.send("Button A", 0.1) # 日付OK
        sleep(0.1)

        self.send("Button HOME", 0.1)
        sleep(0.8)

    def fastOneDay(self, ):
        self.send("Button A", 0.1) # 現在の日付と時刻
        sleep(0.1)

        self.send("LX MIN", 0.05)
        sleep(0.05)

        self.send("LX MIN", 0.05)
        sleep(0.05)

        self.send("LX MIN", 0.05)
        sleep(0.05)

        self.send("LY MIN", 0.1) # 日付を１日進める
        sleep(0.1)

        self.send("Button A", 0.05)
        sleep(0.05)

        self.send("Button A", 0.05)
        sleep(0.05)

        self.send("Button A", 0.05)
        sleep(0.05)

        self.send("Button A", 0.1) # 日付OK
        sleep(0.1)

    def fastTimeLeap(self, n):
        bar = tqdm(total=n)

        self.send("Button B", 0.1)
        self.send("Button B", 0.1)
        self.send("Button B", 0.1) # Initialize

        self.send("Button HOME", 0.1) # Home
        sleep(0.5)

        self.send("LY MAX", 0.1)
        sleep(0.1)

        self.send("LX MAX", 0.1)
        sleep(0.1)

        self.send("LX MAX", 0.1)
        sleep(0.1)

        self.send("LX MAX", 0.1)
        sleep(0.1)

        self.send("LX MAX", 0.1)
        sleep(0.1)

        self.send("Button A", 0.1) # 設定
        sleep(0.1)

        self.send("LY MAX", 2.5)
        self.send("Button A", 0.1) # 本体設定
        sleep(0.1)

        self.send("LY MAX", 0.1)
        sleep(0.1)

        self.send("LY MAX", 0.1)
        sleep(0.1)

        self.send("LY MAX", 0.1)
        sleep(0.1)

        self.send("LY MAX", 0.1)
        sleep(0.1)

        self.send("Button A", 0.1) # 日付と時刻選択
        sleep(0.2)

        self.send("LY MAX", 0.1)
        sleep(0.1)

        self.send("LY MAX", 0.1)
        sleep(0.1)

        count = 0 # count initialize

        self.send("Button A", 0.1) # 現在の日付と時刻
        sleep(0.1)


        self.send("Button A", 0.1)
        sleep(0.1)

        self.send("Button A", 0.1)
        sleep(0.1)

        self.send("LY MIN", 0.1) # 日付を１日進める
        sleep(0.1)

        self.send("Button A", 0.1)
        sleep(0.1)

        self.send("Button A", 0.1)
        sleep(0.1)

        self.send("Button A", 0.1)
        sleep(0.1)

        self.send("Button A", 0.1) # 日付OK
        sleep(0.1)

        count += 1
        bar.update(1)

        while True:
            if count == n:
                break
            if count % 30 == 0:
                self.fastOneDay() # 31日になったら１日進めて日付を１日に戻す

            self.fastOneDay()
            count += 1
            bar.update(1)

        self.send("Button HOME", 0.1)
        sleep(1)
        self.send("Button A", 0.1)
        sleep(0.5)

    def action(self, command):
        if command.split()[0] == "LEAP":
            print("Today is Day {}. Leap {} days.".format(self.today, int(command.split()[1])))
            if self.today == 1:
                self.nDays(int(command.split()[1]))
            else:
                for i in range(int(command.split()[1])):
                    self.oneDay()
            self.today += int(command.split()[1])
            print("Finish. Today is Day {}. ".format(self.today))
        elif command.split()[0] == "RESET":
            print("Today is Day {}. Reset.".format(self.today))
            self.finish(self.today-1)
            self.today = 1
            print("Finish. Today is Day {}. ".format(self.today))
        elif command.split()[0] == "AGAIN":
            print("Today is Day {}. Reset.".format(self.today))
            self.finish(self.today-1)
            self.today = 1
            print("Finish. Leap {} days.".format(int(command.split()[1])))
            self.nDays(int(command.split()[1]))
            self.today += int(command.split()[1])
            print("Finish. Today is Day {}. ".format(self.today))
        elif command.split()[0] == "FASTTIMELEAP":
            print("Have you completed a Rank battle? (yes or no)")
            if input().upper() == "YES":
                print("Did you move into the building? (yes or no)")
                if  input().upper() == "YES":
                    print("Fast TimeLeap for {} days !!".format(int(command.split()[1])))
                    self.fastTimeLeap(int(command.split()[1]))
                else:
                    print("Please move into the building")
                    return
            else:
                print("Please do a Rank battle.")
                return
        elif command == "UP" or command == "I":
            self.send("LY MIN", 0.1)
        elif command == "DOWN" or command == "K":
            self.send("LY MAX", 0.1)
        elif command == "RIGHT" or command == "L":
            self.send("LX MAX", 0.1)
        elif command == "LEFT" or command == "J":
            self.send("LX MIN", 0.1)
        elif command == "EXIT":
            self.send('RELEASE')
            self.ser.close()
        else:
            self.send("Button {}".format(command), 0.1)

        self.today = self.today % 31
        if self.today == 0:
            self.today = 31

        sleep(0.1)

ser = serial.Serial(args.port, 9600)

try:
    send("Button B", 0.1)

    today = 1
    while True:
        print("Command: ", end="")
        command = input().upper()

        if command.split()[0] == "LEAP":
            print("Today is Day {}. Leap {} days.".format(today, int(command.split()[1])))
            if today == 1:
                nDays(int(command.split()[1]))
            else:
                for i in range(int(command.split()[1])):
                    oneDay()
            today += int(command.split()[1])
            print("Finish. Today is Day {}. ".format(today))
        elif command.split()[0] == "RESET":
            print("Today is Day {}. Reset.".format(today))
            finish(today-1)
            today = 1
            print("Finish. Today is Day {}. ".format(today))
        elif command.split()[0] == "AGAIN":
            print("Today is Day {}. Reset.".format(today))
            finish(today-1)
            today = 1
            print("Finish. Leap {} days.".format(int(command.split()[1])))
            nDays(int(command.split()[1]))
            today += int(command.split()[1])
            print("Finish. Today is Day {}. ".format(today))
        elif command.split()[0] == "FASTTIMELEAP":
            print("Have you completed a Rank battle? (yes or no)")
            if input().upper() == "YES":
                print("Did you move into the building? (yes or no)")
                if  input().upper() == "YES":
                    print("Fast TimeLeap for {} days !!".format(int(command.split()[1])))
                    fastTimeLeap(int(command.split()[1]))
                else:
                    print("Please move into the building")
                    continue
            else:
                print("Please do a Rank battle.")
                continue
        elif command == "UP" or command == "I":
            send("LY MIN", 0.1)
        elif command == "DOWN" or command == "K":
            send("LY MAX", 0.1)
        elif command == "RIGHT" or command == "L":
            send("LX MAX", 0.1)
        elif command == "LEFT" or command == "J":
            send("LX MIN", 0.1)
        elif command == "EXIT":
            send('RELEASE')
            ser.close()
        else:
            send("Button {}".format(command), 0.1)

        today = today % 31
        if today == 0:
            today = 31

        sleep(0.1)

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
