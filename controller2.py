#!/usr/bin/env python3
import argparse
import serial
import time
from time import sleep
import datetime
from tqdm import tqdm
import os

parser = argparse.ArgumentParser()
parser.add_argument('port')
parser.add_argument('--clear', type=int, default=1)
args = parser.parse_args()

class Controller:
    def __init__(self, port):
        super().__init__()
        self.today = 1
        self.ser = serial.Serial(port, 9600)

    def send(self, msg, duration=0):
        now = datetime.datetime.now()
        # print(f'[{now}] {msg}')
        self.ser.write(f'{msg}\r\n'.encode('utf-8'))
        sleep(duration)
        self.ser.write(b'RELEASE\r\n')

    def close(self):
        self.ser.close()

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
        sleep(0.11)

        self.send("Button HOME", 0.1)
        sleep(1)

        self.send("Button A", 0.05)
        sleep(0.5)

    def oneDay(self, check=True):
        self.send("Button A", 0.1) # みんなで挑戦
        sleep(3)

        self.leap()

        self.send("Button B", 0.1) # やめる
        sleep(1)

        self.send("Button A", 0.1) # はい
        sleep(4.5)

        if check:
            self.send("Button A", 0.1) # 巣にはなしかける
            sleep(1)

            self.send("Button A", 0.1) # あふれでている
            sleep(0.9)

            self.send("Button A", 0.1) # 2000W手に入れた
            sleep(1)

    def nDays(self, n):
        self.send("Button A", 0.1) # ゲーム起動
        sleep(15)

        self.send("Button A", 0.1) # タイトルA
        sleep(9)

        self.send("Button A", 0.1) # 巣にはなしかける
        sleep(1)

        self.send("Button A", 0.1) # あふれでている
        sleep(1)

        self.send("Button A", 0.1) # 2000W手に入れた
        sleep(1)

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

    def advance1day(self):
        self.send("Button A", 0.1) # ゲーム起動
        sleep(15)

        self.send("Button A", 0.1) # タイトルA
        sleep(8)

        self.send("Button A", 0.1) # 巣にはなしかける
        sleep(1)

        self.send("Button A", 0.1) # あふれでている
        sleep(0.7)

        self.send("Button A", 0.1) # 2000W手に入れた
        sleep(0.7)

        self.send("Button A", 0.1) # みんなで挑戦
        sleep(3)

        self.leap()

        self.send("Button B", 0.1) # やめる
        sleep(1)

        self.send("Button A", 0.1) # はい
        sleep(5)

        self.send("Button X", 0.1) # メニュー開く
        sleep(1.2)

        self.send("Button R", 0.1) # セーブ
        sleep(1.5)

        self.send("Button A", 0.1) # セーブする
        sleep(4)

        self.finish(1)

    def fixseed(self):
        leepday = self.today - 4
        print("Today is day {}. Finish.".format(self.today))
        self.finish(self.today-1)
        self.today = 1
        print("Today is day {}. Leep {} days.".format(self.today, leepday))

        self.send("Button A", 0.1) # ゲーム起動
        sleep(15)

        self.send("Button A", 0.1) # タイトルA
        sleep(9)

        self.send("Button A", 0.1) # 巣にはなしかける
        sleep(1)

        self.send("Button A", 0.1) # あふれでている
        sleep(1)

        self.send("Button A", 0.1) # 2000W手に入れた
        sleep(1)

        for i in tqdm(range(leepday)):
            if i != leepday - 1:
                self.oneDay(True)
                self.today += 1
            else:
                self.oneDay(False)
                self.today += 1

        print("Today is day {}. Save.".format(self.today))

        self.send("Button X", 0.1) # メニュー開く
        sleep(1.2)

        self.send("Button R", 0.1) # セーブ
        sleep(1.5)

        self.send("Button A", 0.1) # セーブする
        sleep(4)

        print("Today is day {}. Finish.".format(self.today))
        self.finish(self.today-1)
        self.today = 1
        print("Today is day {}.".format(self.today))

    def infinityFruits(self, n):
        for i in range(n):
            self.send("Button A", 0.1) # 木に話しかける
            sleep(1)

            self.send("Button A", 0.1) # きのみが取れる木だ
            sleep(1)

            self.send("Button A", 0.1) # はい
            sleep(5)

            self.send("Button A", 0.1) # 落ちてきた
            sleep(1)

            self.send("LY MAX", 0.1) # やめる
            sleep(0.5)

            self.send("Button A", 0.1) # 決定
            sleep(1)

            self.send("Button A", 0.1) # ひろいあげた
            sleep(1)

            self.send("Button A", 0.1) # 手に入れた
            sleep(1)

            self.fastTimeLeap(1)

    def fastOneDay(self):
        self.send("Button A", 0.1) # 現在の日付と時刻
        sleep(0.1)

        self.send("LX MIN", 0.05)
        sleep(0.03)

        self.send("LX MIN", 0.05)
        sleep(0.03)

        self.send("LX MIN", 0.05)
        sleep(0.03)

        self.send("LY MIN", 0.1) # 日付を１日進める
        sleep(0.1)

        self.send("Button A", 0.05)
        sleep(0.03)

        self.send("Button A", 0.05)
        sleep(0.03)

        self.send("Button A", 0.05)
        sleep(0.03)

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

        self.send("LY MIN", 0.1) # 日付を１日進める
        sleep(0.05)

        self.send("Button A", 0.1)
        sleep(0.05)

        self.send("Button A", 0.1)
        sleep(0.05)

        self.send("Button A", 0.1)
        sleep(0.05)

        self.send("Button A", 0.1) # 日付OK
        sleep(0.05)

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

    def fastTimeLeap4S(self, n):
        bar = tqdm(total=n)

        self.send("Button B", 0.1)
        self.send("Button B", 0.1)
        self.send("Button B", 0.1) # Initialize

        self.send("Button HOME", 0.1) # Home
        sleep(0.5)

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

        self.send("LY MIN", 0.1) # 日付を１日進める
        sleep(0.05)

        self.send("Button A", 0.1)
        sleep(0.05)

        self.send("Button A", 0.1)
        sleep(0.05)

        self.send("Button A", 0.1)
        sleep(0.05)

        self.send("Button A", 0.1) # 日付OK
        sleep(0.05)

        count += 1
        bar.update(1)

        while True:
            if count == n:
                break
            if count % 30 == 0:
                self.fastOneDay() # 31日になったら１日進めて日付を１日に戻す
            if count % 8000 == 0:
                self.send("Button HOME", 0.1)
                sleep(1)
                self.send("Button A", 0.1)
                sleep(1)
                self.send("Button HOME", 0.1) # Home
                sleep(0.5)

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

            self.fastOneDay()
            count += 1
            bar.update(1)

        self.send("Button HOME", 0.1)
        sleep(1)
        self.send("Button A", 0.1)
        sleep(0.5)

    def pokejob(self, jobtime=None):
        self.send("Button A", 0.1)  # 一番上選択
        sleep(1)

        self.send("Button A", 0.1)  # 受けますか？ － はい
        sleep(1.5)

        self.send("Button A", 0.1)  # ボックスに移動します
        sleep(1.6)

        self.send("Button Y", 0.1)  # 操作切り替え
        sleep(0.3)

        if jobtime is None: # 経験値
            c = ["LX MAX", "LX MIN", "LX MAX", "LX MIN"]
            for i in range(4):
                for j in range(5):
                    self.send("Button A", 0.05)
                    sleep(0.05)
                    self.send(c[i], 0.05)
                    sleep(0.05)
                self.send("Button A", 0.1)
                sleep(0.1)
                self.send("LY MAX", 0.1)
                sleep(0.1)
        else: # 努力値
            self.send("LY MAX", 0.1)
            sleep(0.1)

            self.send("LY MAX", 0.1)
            sleep(0.1)

            self.send("LY MAX", 0.1)
            sleep(0.1)

            self.send("Button A", 0.1)
            sleep(0.1)

        self.send("Button B", 0.1)  # おくりだす
        sleep(1.8)

        self.send("Button A", 0.1)  # はい
        sleep(3)

        self.send("Button A", 0.1)  # おくりだす
        sleep(1)

        if jobtime is not None:
            for i in range(jobtime):
                self.send("LY MAX", 0.1)
                sleep(0.5)

        self.send("Button A", 0.1)  # 一日
        sleep(10)

        self.send("Button A", 0.1)  # 向かいました
        sleep(0.8)

        self.send("Button A", 0.1)  # がんばってきてね
        sleep(0.5)

        # １日＋１分時渡り
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

        self.send("LY MIN", 0.06) # 分を１分進める
        sleep(0.1)

        self.send("Button A", 0.06)
        sleep(0.05)

        self.send("Button A", 0.08) # 日付OK
        sleep(0.2)

        self.send("Button HOME", 0.05)
        sleep(1)

        self.send("Button A", 0.05)
        sleep(1)

        self.send("Button A", 0.1)
        sleep(14)
        self.send("Button A", 0.1)  # 帰ってきました
        sleep(1)

        if jobtime is None:
            self.send("Button A", 0.1)  # とても活躍した
            sleep(2)
        else:
            sleep(1.5)

        self.send("Button A", 0.1)  # 経験値もらった
        sleep(3)

        self.send("Button A", 0.1)  # なんとかお手伝いを
        sleep(0.8)

        self.send("Button A", 0.1)  # やりとげたようです
        sleep(1)

        self.send("Button A", 0.1)  # 次はもっと
        sleep(1)

        self.send("Button A", 0.1)  # わたしたいものが
        sleep(1)

        self.send("Button A", 0.1)  # お礼として
        sleep(1)

        self.send("Button B", 0.1)
        sleep(1)

        self.send("Button A", 0.1)  # またの
        sleep(1)

        self.send("Button A", 0.1)  # ロトミに話しかける
        sleep(1)

        self.send("Button A", 0.1)
        sleep(1)

        self.send("LY MAX", 0.1)
        sleep(0.1)

        self.send("LY MAX", 0.1)
        sleep(0.1)

        self.send("Button A", 0.1)  # ポケジョブ選択
        sleep(4)

        self.send("Button A", 0.1)  # 新しいお手伝い
        sleep(0.5)

        pass

    def nojob(self):
        self. send("Button B", 0.1)
        sleep(1)

        self. send("Button B", 0.1)
        sleep(1)

        self.fastTimeLeap(1)
        sleep(2)

        self.send("Button A", 0.1)  # ロトミに話しかける
        sleep(2)

        self.send("Button A", 0.1)
        sleep(2)

        self.send("LY MAX", 0.1)
        sleep(0.1)

        self.send("LY MAX", 0.1)
        sleep(0.1)

        self.send("Button A", 0.1)  # ポケジョブ選択
        sleep(4)

        self.send("Button A", 0.1)  # 新しいお手伝い
        sleep(0.5)

    def effort(self, V, n):
        vposition = {"S":1, "D": 2, "C":3, "B":4, "A":5, "H":6}
        move = vposition[V.upper()]

        n2time = [96, 48, 32, 16, 12, 8, 4]
        timeList = [0, 0, 0, 0, 0, 0, 0]

        if n >= 252:
            timeList[0] = 3
        else:
            for i, d in enumerate(n2time):
                timeList[i] = int(n / d)
                n = n - timeList[i] * n2time[i]
                if n == 0:
                    break

        for i in range(len(timeList)):
            print("{}:{}  ".format(n2time[i], timeList[i]), end="")
        print("")
        sleep(1)

        bar = tqdm(total=n)

        for i, j in enumerate(timeList):
            for k in range(j):
                for m in range(move):
                    self.send("LY MIN", 0.1)
                    sleep(0.5)
                self.pokejob(jobtime=i)
                bar.update(n2time[i])
        bar.close()

    def autoRotomi(self):
        self.send("Button A", 0.1) #ロトミ起動
        sleep(0.8)

        self.send("Button B", 0.1)
        sleep(0.5)

        self.send("LY MAX", 0.1)
        sleep(0.5)

        self.send("Button A", 0.1)
        sleep(0.6)

        self.send("Button A", 0.1)
        sleep(1)

        self.send("Button A", 0.1)
        sleep(1)

        self.send("Button A", 0.1)
        sleep(1)

        self.send("Button A", 0.1)
        sleep(1)

        self.send("Button A", 0.1)
        sleep(1)

        self.send("Button A", 0.1)
        sleep(0.8)

        self.send("Button A", 0.1)
        sleep(2.2)
        #レポート
        self.send("Button B", 0.1)
        sleep(1)

        self.send("Button B", 0.1)
        sleep(1)

        self.send("Button B", 0.1)
        sleep(1)

        self.send("Button B", 0.1)
        sleep(1)

        self.send("Button B", 0.1)
        sleep(1)

        self.send("Button B", 0.1)
        sleep(1)

        self.send("Button B", 0.1)
        sleep(1)

        self.send("Button B", 0.1)
        sleep(1)

        self.send("Button B", 0.1)
        sleep(1.5)
        #待機
        self.send("Button B", 0.1)
        sleep(1)

        self.send("Button B", 0.1)
        sleep(1)

        self.send("Button B", 0.1)
        sleep(1)

        self.send("Button B", 0.1)
        sleep(1)

        self.send("Button B", 0.1)
        sleep(1)

        self.send("Button B", 0.1)
        sleep(1)

        self.send("Button B", 0.1)
        sleep(1)

        self.send("Button B", 0.1)
        sleep(1)

        self.send("Button B", 0.1)
        sleep(1)

        self.send("Button B", 0.1)
        sleep(0.7)
        #ロトミ閉じる

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

        self.send("Button A", 0.06) # 現在の日付と時刻
        sleep(0.1)



        self.send("LY MAX", 0.1) #年号1つもどす
        sleep(0.1)

        self.send("Button A", 0.05)
        sleep(0.05)

        self.send("Button A", 0.05)
        sleep(0.05)

        self.send("Button A", 0.05)
        sleep(0.05)

        self.send("Button A", 0.05)
        sleep(0.05)

        self.send("Button A", 0.05)
        sleep(0.05)

        self.send("Button A", 0.1) #日付OK
        sleep(0.1)


        self.send("Button A", 0.05)
        sleep(0.05)

        self.send("LX MIN", 0.05)
        sleep(0.05)

        self.send("LX MIN", 0.05)
        sleep(0.05)

        self.send("LX MIN", 0.05)
        sleep(0.05)

        self.send("LX MIN", 0.05)
        sleep(0.05)

        self.send("LX MIN", 0.05)
        sleep(0.05)

        self.send("LX MIN", 0.05)
        sleep(0.05)

        self.send("LY MIN", 0.1) #年号1つすすめる
        sleep(0.1)

        self.send("Button A", 0.05)
        sleep(0.05)

        self.send("Button A", 0.05)
        sleep(0.05)

        self.send("Button A", 0.05)
        sleep(0.05)

        self.send("Button A", 0.05)
        sleep(0.05)

        self.send("Button A", 0.05)
        sleep(0.05)

        self.send("Button A", 0.1) #日付OK
        sleep(0.5)


        self.send("Button HOME", 0.1) #ゲームに戻る
        sleep(1.0)

        self.send("Button HOME", 0.1)
        sleep(2.0)

    def help(self):
        with open("./readme.txt", "r") as f:
            print(f.read())

    def action(self, command):
        command = command.upper()
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
        elif command.split()[0] == "FASTTIMELEAP" or command.split()[0] == "FTL":
            if len(command.split()) == 3:
                check = bool(command.split()[2])
            else:
                check = False
            if not check:
                if input("Have you completed a Rank battle? (yes or no)").upper() != "YES":
                    print("Please do a Rank battle.")
                    return
            if not check:
                if  input("Did you move into the building? (yes or no)").upper() != "YES":
                    print("Please move into the building")
                    return
            print("Fast TimeLeap for {} days !!".format(int(command.split()[1])))
            self.fastTimeLeap(int(command.split()[1]))
        elif command.split()[0] == "FASTTIMELEAP4S" or command.split()[0] == "FTL4S":
            if len(command.split()) == 3:
                check = bool(command.split()[2])
            else:
                check = False
            if not check:
                if input("Have you completed a Rank battle? (yes or no)").upper() != "YES":
                    print("Please do a Rank battle.")
                    return
            if not check:
                if  input("Did you move into the building? (yes or no)").upper() != "YES":
                    print("Please move into the building")
                    return
            print("Fast TimeLeap for {} days !!".format(int(command.split()[1])))
            self.fastTimeLeap4S(int(command.split()[1]))
        elif command.split()[0] == "ADVANCE":
            print("Today is Day {}. Reset.".format(self.today))
            self.finish(self.today-1)
            self.today = 1
            print("Finish. Advance 1 day.")
            self.advance1day()
        elif command.split()[0] == "SETTODAY":
            self.today = int(command.split()[1])
            print("Today is Day {}. ".format(self.today))
        elif command.split()[0] == "POKEJOB":
            self.pokejob()
        elif command.split()[0] == "NOJOB":
            self.nojob()
        elif command.split()[0] == "EFFORT":
            self.effort(command.split()[1], int(command.split()[2]))
        elif command.split()[0] == "WAIT":
            sleep(float(command.split()[1]))
        elif command == "RESETTODAY":
            self.today = 1
        elif command == "FIXSEED":
            print("Today is Day {}. Reset.".format(self.today))
            self.fixseed()
            print("Today is Day {}. ".format(self.today))
        elif command.split()[0] == "ROTOMI":
            n = input("How long ? (Type \"number\" or \"inf\")")
            if n == "inf":
                while True:
                    self.autoRotomi()
            else:
                for i in tqdm(range(int(n))):
                    self.autoRotomi()
        elif command == "HELP":
            with open("./readme.txt", "r") as f:
                print(f.read())
        elif command.split()[0] == "HOLD":
            c = command.split()[1]
            t = float(command.split()[2])
            if c == "UP" or c == "U":
                self.send("LY MIN", t)
            elif c == "DOWN" or c == "J":
                self.send("LY MAX", t)
            elif c == "RIGHT" or c == "K":
                self.send("LX MAX", t)
            elif c == "LEFT" or c == "H":
                self.send("LX MIN", t)
        elif command == "UP" or command == "U":
            self.send("LY MIN", 0.1)
        elif command == "DOWN" or command == "J":
            self.send("LY MAX", 0.1)
        elif command == "RIGHT" or command == "K":
            self.send("LX MAX", 0.1)
        elif command == "LEFT" or command == "H":
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


def main():
    c = Controller(args.port)

    try:
        c.send("Button B", 0.1)
        memory = None
        memory2 = None
        prevCommand = None

        while True:
            command = input("Command: ").upper()

            if args.clear is 1:
                os.system('clear')
                print("\n"*30)
                os.system('clear')
                print("Command: {}".format(command))

            if command == "":
                continue
            if command.split()[0] == "READ":
                with open("./scriptTxt/{}".format(command.split()[1]), "r") as f:
                    command = f.readline()
                    while command:
                        print(command[:-1])
                        c.action(command[:-1])
                        command = f.readline()
                    print("finish TXT command !")
            elif command.split()[0] == "RECORD":
                commands = ""
                command = input("Recording Command: ").upper()
                t = time.time()
                while command.split()[0] != "STOP":
                    c.action(command)
                    commands += command + "\n"
                    command = input("Recording Command: ").upper()
                    commands += "WAIT {:.2f}\n".format(time.time() - t)
                    t = time.time()
                filename = input("Finish Recording !\nWhat is the file name?: ")

                with open("./scriptTXT/{}".format(filename), "w") as f:
                    f.write(commands)
                    print("Export commands!")
            elif command == "MEMORY":
                memory = input("Memory Command: ")
            elif command == "MEMORY2":
                memory2 = input("Memory2 Command: ")
            elif command == "M":
                print("Memory Command is \"{}\"".format(memory))
                c.action(memory)
            elif command == "N":
                print("Memory2 Command is \"{}\"".format(memory2))
                c.action(memory2)
            elif command == "S":
                c.action(prevCommand)
            else:
                c.action(command)
                prevCommand = command

    except KeyboardInterrupt:
        c.send('RELEASE')
        c.close()

if __name__ == "__main__":
    main()
