# SWpokeCon
ポケットモンスター ソード・シールドにおけるキー入力や作業の自動化を行うPythonスクリプト

## 必要なもの
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

### LEAP
旧時渡りすることができます。巣穴にねがいのかたまりを投げ込んだ状態かつ、巣穴からワットを回収していない状態かつ、Aボタンで回収できる位置に立った状態でソフトを落とし、ポケモンにカーソルを合わせてからこのコマンドを実行します。LEAPを一度行った状態であれば、ゲーム起動後でもこのコマンドを実行することができます

    Command
        LEAP day
    Ex. LEAP 3
        ３日時渡りします

### RESET
ゲームを終了し、日付を元に戻します。

    Command
        RESET
    Ex. RESET
        日付を１日に戻して、ゲームを終了します。

### AGAIN
ゲームを終了した上で、任意の回数時渡りをします

    Command
        AGAIN day
    Ex. AGAIN 3
        日付を１日に戻してゲームを終了し、新たにゲームを起動し３回時渡りをします。

### FASTTIMELEAP
高速で新時渡りをします。**建物内**かつ**ランクマッチを行った**状態で実行してください。

    Command
        FASTTIMELEAP day
            or
        FTL day
        
### FASTTIMELEAP4S
FASTTIMELEAPのSwitch Lite対応版です。およそ8000回時渡りすると、一度ゲーム画面に戻ります。

    Command
        FASTTIMELEAP4S day
            or
        FTL4S day

### POKEJOB
最高レベルのポケジョブを一度行います。**新時渡りができる状態**で実行するようにしてください。
#### 事前準備
ボックス１に全単タイプのポケモンを上から3行使って配置してください。上から4行目に育成したポケモンを配置してください。
#### 実行前に
ポケジョブの画面を開き、最高難易度のポケジョブにカーソルが合った状態にしてください。
#### 実行
POKEJOBと打ち込むと自動的にポケジョブが実行されます。

    Command
        POKEJOB

### NOJOB
最高レベルのポケジョブが出ていないときのためのコマンドです。**新時渡りができる状態**で実行するようにしてください。
ポケジョブの画面でNOJOBコマンドを実行することで、仕事一覧を更新します。

    Command
        NOJOB

### EFFORT
ポケジョブを利用して自動的に努力値振りを行います。お手伝いに行かせる時間の計算も自動で行います。**新時渡りができる状態**で実行するようにしてください。
ポケジョブ画面を開き、一番上の仕事にカーソルが合った状態で実行してください。

    Command
        EFFORT V箇所 n
    Ex. EFFORT A 252
        Aに252の努力値を振ります


## 資料
「ポケットモンスター ソード・シールド」におけるポケモンのタマゴ孵化や「かえんだま」入手作業を自動化する – 無能ブログ  
https://blog.cheena.net/2533

NintendoSwitchをPCから操作する - おいら屋ファクトリー  
https://blog.feelmy.net/control-nintendo-switch-from-computer/

## ライセンス
[MITライセンス](https://github.com/cheenanet/pokemon-swsh-scripts/blob/master/LICENSE)
