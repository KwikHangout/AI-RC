---
title: "jetson"
chapter: true
weight: 1
---

{{<toc>}}

## Jetson Nano ドンキカー

- １号機、２号機

  {{<img src="./img/IMG_0775.jpeg" width="400">}}

  {{<img src="./img/IMG_0776.jpeg" width="400">}}

- バッテリー、充電器、放電器

  {{<img src="./img/IMG_0778.jpeg" width="400">}}

- モバイルバッテリー、USB AC アダプター

  {{<img src="./img/IMG_0779.jpeg" width="400">}}

- 無線スポット DONKEY001

  {{<img src="./img/IMG_0787.jpeg" width="400">}}

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
    buttonA([Aボタン 緊急停止])
    buttonY([Yボタン 削除5秒])
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

  WifiSpot[無線LAN DONKEY001]
  WifiSpot -.- Donkeycar
  WifiSpot -.- pc

  ```

JOYSTICk 拡大写真

  {{<img src="./img/2024-01-09-15-59-23.png" width="800">}}

----

## ワークフロー

1. 学習のための走行データの取得

   - 15-20周 5-10分の走行を実施

     > 5分で6000データセットが集まります。

    ```mermaid
    graph TB

    subgraph ラジコン
      hw[電源ON ラジコン、ゲームパッド]
    end

    subgraph PC
      del[前回のデータを消す del_data]
      run[走行 run_car]
      stop[終了 run_carをキャンセル]
    end

      hw -.-> del
      del -.-> run

    subgraph ゲームパッド
      drive[走行 15周 Bボタンで記録 On/Off]
    end

    run -.->drive
    drive -.-> stop
    ```

    <div style="page-break-before:always"></div>

1. 学習

    ```mermaid
    graph TB

    subgraph ラジコン
      state[停止状態 電源はそのままでOK]
    end

    subgraph PC
      check["データ数の確認 ls -l ./data/images | wc-l"]
      train[学習 run_train 10-20分]
    end
    ```

1. AI 走行

    ```mermaid
    graph TB

    subgraph ラジコン
      stateOK[自動走行状態]
      stateNG[衝突して止まった]
    end

    subgraph PC
      auto[AI走行 run_ai]
      stop[終了 run_aiをキャンセル]
    end

    subgraph ゲームパッド
      drive[startボタンで走行切り替え]
      userangle[ジョイスティックで後進させて位置を戻す]
    end

    auto -.->drive
    drive-.->stateOK
    stateOK -.->stateNG
    stateNG -. startボタン or Aボタン.->userangle
    userangle -.startボタン.-> drive
    stateOK -.-> stop
    ```

    <div style="page-break-before:always"></div>

1. 状態チェック

    ```mermaid
    graph RL

      subgraph ラジコン
        battery[ラジコン バッテリー]
        wheels[車輪]
        subgraph jetson
          WiFi
          camera[カメラ]
          mobilebattery[モバイルバッテリ]
          donkey[donkey web server]
          jupyter[jupyter server]
        end
      end

      subgraph ゲームパッド
        batterycell[乾電池]
        mode[モード]
        inut[XInputとDirectInpu]
      end

      subgraph 予備バッテリー
        battriesUsed[バッテリー 使用済]
        battriesNext[交換用バッテリー]
        adapterCharge[充電器]
        adapterDischarge[放電機]

        adapterCharge -.- battriesNext
        adapterDischarge -.- battriesUsed
      end

      subgraph PC
        chrome[ブラウザ]
      end

      WiFiSpot[無線LANスポット Dokey001]

      chrome -. "http 8888" .- jupyter
      chrome -. "http 8887" .- donkey

    ```

    <div style="page-break-before:always"></div>

1. デモ・説明

  ```mermaid
  graph LR


　subgraph 操作
    subgraph phase1[事前準備]
      drive([走行データ取得 run_car])
      train([学習 run_train])
      test1[問題なく走ることを確認 run_ai]
      test2[パイロンを外して 変化のあることを確認]
      test3[パイロンを戻して 元に戻ることを確認]
    end
    subgraph phase2[デモ/説明]
      demo0([パイロンを外して走行])
      demo1([パイロン設置])
      demo2([通常走行])
    end

    demo0-.->demo1
    demo1-.->demo2
  end

   drive -.-> train
   train -.->test1
   test1 -.->test2
   test2 -.->test3

  subgraph cars[ドンキーカー]
    car1[１号機 - パイロンなしで学習]
    car2[２号機 - パイロンありで学習]
  end

  subgraph PC
    tab1[ブラウザ http:<１号機IP>:8888]
    tab2[ブラウザ http:<2号機IP>:8888]
  end

  cars -.- phase1
  PC -.- phase1

  ```


  - [ ] ラジコンカーとJetsonが走行可能な状態か？

     run_car または run_aiを実行後に、http://<ip>:8887 をブラウザで開いてみてください。

     jupyternoteのブラウザ画面のrun_car/run_aiのログにエラーが出力されていないかを確認してください。

  - [ ] 走行データの記録ができたか？

    画像ファイルの数を確認する

    ```
     ls -l ~/mycar/data/images | wc-l
    ```

 - [ ] 学習ができたか？

    run_trainのログで状態を確認してください。

    - epocの出力が正常に終了したことを確認してください。

      画像ファイルがないなどのエラーの場合は、すぐに終了します。

    - mypilot.h5が保存された旨のログが出力されます。


- [ ] 自動走行が期待された結果にならない。

    学習データに正常な走行には不必要な衝突などのデータが混じっている可能性があります。

    - raspi用PCに構築された donkeycarの環境で、donkey uiを実行してデータを確認できます。

      > raspiの手順を参考 raspi.md

      1. raspi用ホストPCで conda activate donkey
      1. rsyncでホストPCに mycar/dataフォルダをコピーする。
      1. donkey uiをたちあげて、tab managerで確認

          ```
          conda activate donkey
          cd ~/projects/mycar

          rsync -rv --progress --partial jetson@<IP>:~/mycar/data/  ./data/

          donkey ui
          ```


------

## 事前準備

- 展示用の無線LANスポット(DONKEY001) の電源をON

- 搭載されたJetson Nanoとラジコンカーのそれぞれのバッテリーが十分に充電しておく

  - ラジコンカーバッテリー
  - jetson nano用バッテリー

- ラジコンとJetsonNanoの電源をONにします。

  - 無線LANスポット: DONKEY001に自動で接続されます。

      > インターネットに接続していない無線LANスポットです

      >　パスワード: DONKEY1111111

    - 固定IP デモ１号機と２号機に割り振られています

      - 192.168.100.101
      - 192.168.100.102

<div style="page-break-before:always"></div>

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
    - Yボタン (削除5秒)

      衝突などのエラー操作があった時に、直前の5秒のデータを消去します

1. run_train.sh
1. run_ai.sh

    ロードするまで１０秒弱。 8887ポートで下記のDonkey Monitorが開きます。

    - Joystick

      - startボタン 切り替え 手動・Auto

        Select button switches modes - "User, Local Angle, **Local(angle and throttle)**"

        startボタンで走行が手動・自動が切り替わります。

      - Aボタン(緊急停止)

        衝突した場合は Aボタンを押す。 startボタンでユーザ操作またはLocal Angleにして、後退させて再度自動走行を実施

    - http://192.168.100.101:8887

      Donkey Monitorでも　 mode: Localを選択することで　AI自動走行が実施されます。

      {{<img src="./img/2024-01-06-14-06-06.png" width="1080">}}

