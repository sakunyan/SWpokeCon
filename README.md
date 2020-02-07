# SWpokeCon
ポケットモンスター ソード・シールドにおけるキー入力や作業の自動化を行うPythonスクリプト

## 条件
- USB搭載のマイクロコンピュータ（CPUに atmega16u2 or atmega32u4 を搭載したもの）
- USBシリアル変換アダプタ
- microUSBケーブル
- [ebith/Switch-Fightstick](https://github.com/ebith/Switch-Fightstick)

## 起動
wsl上で`python3 controller2.py /dev/ttySX` (XはCOM portの数字)

## コマンド
### Ordinary command
ただ普通にコマンドを送信します。送信時間はおよそ0.1秒です

    Comand
        just input commmand!
        Exception
            LY_MIN : U
            LY_MAX : J
            LX_MIM : H
            LX_MAX : K

    Ex. a
        ”A"キーを送ります。

### HOLD
任意の時間キーをホールドします

    Command
        HOLD key time

    Ex. HOLD LX_MAX 3
        上キーを３秒送信します

### READ
テキストファイルに記述されているコマンド列を順に実行することができます

    Command
        RECORD
        STOP

    Ex. RECORD
        a
        b
        a
        STOP
        test.txt
        text.txtファイルにa, b, aのコマンドが記録されます


## 資料
「ポケットモンスター ソード・シールド」におけるポケモンのタマゴ孵化や「かえんだま」入手作業を自動化する – 無能ブログ  
https://blog.cheena.net/2533

NintendoSwitchをPCから操作する - おいら屋ファクトリー  
https://blog.feelmy.net/control-nintendo-switch-from-computer/

## ライセンス
[MITライセンス](https://github.com/cheenanet/pokemon-swsh-scripts/blob/master/LICENSE)
