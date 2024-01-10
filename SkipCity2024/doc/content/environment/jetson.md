---
title: "jetson"
chapter: true
weight: 1
---


### Jetson Nano ドンキカー

## 概念図

  ```mermaid
  graph TB
  subgraph Donkeycar
    subgraph jetson[Jetson nano]
      jupyter[jupyter service]
      app[donkeycar v4.5.0]
    end
    mobile([モバイルバッテリー])
    yokomo([ラジコンバッテリー])
    switch([ラジコンスイッチ])
    stirring
    motor
    controller
    app-.-controller
    controller -.- motor
    controller -.- stirring
  end

  subgraph joystick[ゲームパッド]
    buttonB([Bボタン 記録 On/Off])
    buttonA([Aボタン 削除5秒])
    start([startボタン 切り替え 手動・Auto])
    stickL([左ジョイスティック ハンドル])
    stickR([右ジョイスティック アクセル])

  end

  joystick -.- app

  subgraph pc[PC]
    browser([chrome browser <br> del_data<br>run_car<br>run_train<br>run_ai])
  end
  browser -. http://host_addr:8888 .-jupyter

  USBAdapter([USB充電])
  mobile -.- USBAdapter
  LiFeAdapter([充電器/放電器])
  yokomo -.-LiFeAdapter

  WifiSpot[無線LAN DONKEY0001]
  WifiSpot -.- Donkeycar
  WifiSpot -.- pc

  ```

{{<img src="./img/2024-01-09-15-49-16.png" width="800">}}

{{<img src="./img/2024-01-09-15-59-23.png" width="800">}}

------

## 事前準備

- 展示用の無線LANスポット(DONKEY001) の電源をON

- 搭載されたJetson Nanoとラジコンカーのそれぞれのバッテリーが十分に充電しておく

  - ラジコンカーバッテリー
  - jetson nano用バッテリー

- ラジコンとJetsonNanoの電源をONにします。

  - 無線LANスポット: DONKEY001に自動で接続されます。

      > インターネットに接続していない無線LANスポットです

      >　パスワード: 1が８個

    - 固定IP デモ１号機と２号機に割り振られています

      - 192.168.100.101
      - 192.168.100.102

----
## 操作

PCブラウザでJupyter notebookからドンキカーに走行データ記録、学習、自走走行のコマンドを実行します。

{{<img src="./img/2024-01-06-09-58-11.png" width="600">}}

ラジコンカーに搭載されたJetson nanoにある以下のシェルコマンドがJupyter notebook経由で使用可能になっています。

PCを無線LANスポット: DONKEY001に繋ぎ、Chormeブラウザで　http://<Jetson nano IP アドレス>:8888ポートでjupyter notebookを開きます。

例 １号機

http://192.168.100.101:8888

1. del_data.sh
1. run_car.sh

    ゲームパッド
    - Bボタン(記録 on/off)
    - Aボタン

      衝突などのエラー操作があった時に、直前の10秒のデータを消去します


1. run_train.sh
1. run_ai.sh

    ロードするまで１０秒弱。 8887ポートで下記のDonkey Monitorが開きます。


    - Joystick

      Select button switches modes - "User, Local Angle, **Local(angle and throttle)**"

      - F710 では startボタンで走行が手動・自動が切り替わります。

    - http://192.168.100.101:8887

      Donkey Monitorでも　 mode: Localを選択することで　AI自動走行が実施されます。

      {{<img src="./img/2024-01-06-14-06-06.png" width="1080">}}

