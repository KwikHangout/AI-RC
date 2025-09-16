---
title: "TatamiRacer DIY"
chapter: true
weight: 1
---

2025 8月現在

オリジナルのReadmeを参考に Raspi Zero 2 Wで組み立ててみました。作業メモです。

  [github.com/covao/TatamiRacer - Japanese](https://github.com/covao/TatamiRacer/blob/master/README_JP.md)

  > オリジナルの手順を参考に進めてください

----

## Raspberry Pi 本体価格

| 製品名 | 価格 | リンク |
|:---|:---|:---|
| Raspberry Pi 4 Model B | ￥9,200 | [商品ページ](https://akizukidenshi.com/catalog/g/g114839/) |
| Raspberry Pi 3 Model A+ | ￥4,620 | [商品ページ](https://akizukidenshi.com/catalog/g/g114878/) |
| Raspberry Pi Zero 2 W | ￥3,190 | [商品ページ](https://akizukidenshi.com/catalog/g/g117398/) |


## Tatami 3Dパーツ

PCBWayの3Dプリントサービスを利用しました

$35=¥5000 (送料 $25)

<img src="./img/2025-07-24-10-00-32.png" width="600" class="popup-image">


## F710 (ゲームパッド)

  ¥5,200 [Amazon](https://www.amazon.co.jp/dp/B00CDG7994/?th=1)

---

## 合計 24,938円  ~ 30,938円

- Raspi 3200~9200円
- PCBWay 5000円
- F710　 ¥5,200
- 部品費 11,538円

### 部品価格一覧（BOM）

| 品名 | 価格 | リンク / 備考 |
| --- | ---: | --- |
| カメラ V1 (OV5647) | ¥1,400 | RasTech Raspberry Pi Camera Module (5MP) https://www.amazon.co.jp/exec/obidos/ASIN/B086MK17K5/beatnix06-22/ |
| バッテリー (明誠 C0303 4000mAh) | ¥1,450 | https://www.amazon.co.jp/dp/B07Q5M3CLQ/?th=1 <br> (Type A→C充電) |
| DCモーター用 Hブリッジ (L298N) | ¥700 | https://www.amazon.co.jp/dp/B083DT2DMV/ |
| ピンヘッダー (オス 90度 40ポジション×2) | ¥700 | https://www.amazon.co.jp/dp/B00V4V703O/ |
| 130 DC モーター (Tamiya No.28) | ¥1,400 | https://www.amazon.co.jp/dp/B005AFBLIA/ |
| サーボ (TowerPro SG90) | ¥1,200 | https://amzn.asia/d/2tIKGHg <br>標準 0.1s / 60度 |
| ミニ四駆 キット (ぞうさん 5:1ギア) | ¥1,500 | https://www.amazon.co.jp/dp/B08VX3W3Q6/ |
| ローラーパーツ (低摩擦プラローラーセット) | ¥220 | タミヤ GP.381 (15381) https://www.amazon.co.jp/dp/B001E40PXI/ |
| タミヤ ステンレスビスセット | ¥300 | GP.508 (15508) M2x15/16 推奨 <br> https://amzn.asia/d/e0r3VGH|
| タミヤ 72mm シャフト (Black Reinforced Shaft) | ¥150 | GP.417 (15417) https://www.amazon.co.jp/dp/B003GALRS0/ |
| ジャンパーケーブル (メス-メス 10cm) | ¥700 | - |
| SDカード | ¥800 | (目安) |
| 短いUSBケーブル (A‑microB 10cm) | ¥561 | https://www.switch-science.com/products/2844 (モバイルバッテリー→Raspi Zero) |
| USB → Micro‑B 変換アダプタ | ¥357 | https://www.switch-science.com/products/3702 (F710ドングル用) |
| 合計（概算) | ¥11,538 |  |

---

## Raspi Zero用

- [x] rapi zero camera cable
- [x] USB micro to A for raspi zero power
- [x] USB micro to A fro F710 donggle


- 短いUSBケーブル（A-microBタイプ）10cm で モバイルバッテリーからraspi zeroに給電します

  https://www.switch-science.com/products/2844
  561円

  <img src="./img/2025-08-04-10-03-44.png" width="200" class="popup-image">


- USBをMicro-Bへ変換するアダプタ これは F710のゲームパッドのUSBドングルを micro-Bに接続するために必要です。

  <br>
  https://www.switch-science.com/products/3702

  <img src="./img/2025-08-04-09-59-32.png" width="200" class="popup-image">

- Zeo用カメラケーブル V1キット(1,390円)に含まれている

  https://www.amazon.co.jp/-/en/RasTech-Raspberry-Camera-Megapixels-ZERO1-3/dp/B086MK17K5

  <img src="./img/2025-08-04-10-00-40.png" width="200" class="popup-image">



---
その他 道具

- [x] ニッパー
- [x] ハンダこて

---

## Deliveries

- [x] raspi
- [x] sdcard
- [x] ピンヘッダー
  どこで使う？
- [x] ジャンパーケーブル (メス)

  <img src="./img/2025-07-24-13-22-32.png" width="400" class="popup-image">

---

ゆうパケット - Yahoo

- [x] タミヤパーツ

  <img src="./img/2025-07-26-09-28-17.png" width="600" class="popup-image">

ヤマト from amaozn
- [x] 503-6072152-2431021

  <img src="./img/2025-07-26-09-33-46.png" width="600" class="popup-image">

- [x] 503-9357226-4950233

  <img src="./img/2025-07-26-09-29-21.png" width="600" class="popup-image">

- [x] 503-7522781-5623054

  <img src="./img/2025-07-26-09-30-53.png" width="600" class="popup-image">

- [x] 503-1516758-2159868

  <img src="./img/2025-07-26-09-35-21.png" width="600" class="popup-image">

- [x] DCモーター用/Hブリッジ

  <img src="./img/2025-07-26-10-02-30.png" width="600" class="popup-image">


----

## ミニ四駆 マシンセッティングガイド

https://www.tamiya.com/japan/cms/mini4wdsettingguide_basic.html

  https://www.youtube.com/watch?v=t5xuVLtgMZA

http://www.miniyonku.net/assemble-miniyonku

----

ミニ四駆「ぞうさん」（正式型番 95569、VZシャーシ）のキットには、**標準のノーマル（標準回転数）タイプの 130φ モーター**が付属しています。これはタミヤの一般的なキットに搭載される「SMC 標準モーター」であり、**Low RPM Type 130** とは異なります ([Tamiya][1])。

* 「Low RPM Type 130」とは、回転数が抑えられたトルク重視の特殊モーターで、標準キットには基本的に採用されていません。
* ぞうさんキットに標準で入っているのは「ノーマルモーター（SMC製）」で、**速度もトルクも中程度のバランス型**です ([ムーチョのミニ四駆ブログ][2], [ミニ四駆マスターズ][3], [Tamiya][1])。

そのため、ご質問の「Low RPM Type 130 ですか？」に対しては、**いいえ**となります。キット付属のモーターは「**Low RPM Type**」ではなく、**標準のノーマルタイプ**です。

もしトルク重視の低速仕様モーターをお探しであれば、例えば「トルクチューン2」などへの交換が可能です。ノーマルより遅めですが、安定したカーブや上り坂での走行に適しています ([ムーチョのミニ四駆ブログ][4])。

---

### ✅ まとめ

| 項目              | キット付属のモーター                 |
| --------------- | -------------------------- |
| モータータイプ         | 標準ノーマル（SMC製 Type 130）      |
| Low RPM Type か？ | **いいえ**                    |
| 性能傾向            | バランス型（中速・中トルク）             |
| トルク重視で低回転が欲しい場合 | 「トルクチューン2 モーター」などへの交換をおすすめ |

ご不明点や他のモーターとの比較などもあれば、お気軽にどうぞ！

- [1](https://www.tamiya.com/japan/products/95569/index.html?utm_source=chatgpt.com) タミヤ ミニ四駆特別企画　ミニ四駆ぞうさん | タミヤ"
- [2](https://www.mini4wd.tech/archives/mini4wd-motor-recommendation-list.html?utm_source=chatgpt.com) 〖2025年〗ミニ四駆のおすすめモーターランキング｜種類と選び方も紹介 | ムーチョのミニ四駆ブログ"
- [3](https://mini4-masters.com/mini-yonku-shoshinsha-kaumono-guide/?utm_source=chatgpt.com) ミニ四駆を始める初心者が買うもの全部見せます！予算3000円から楽しめる！速く走らせるコツも‼｜ミニ四駆マスターズ"
- [4](https://www.mini4wd.tech/archives/mini4wd-animalseries-modification.html?utm_source=chatgpt.com) 〖ミニ四駆アニマルシリーズ〗ぞうさんのポテンシャル｜簡単な改造パーツで安定した走りに | ムーチョのミニ四駆ブログ"

----
## 組み立て

部品一覧
<img src="img/parts_purchased.png" width="1600">
<img src="img/parts_all.png" width="1600">

ミニ４駆の車体キットに入っている部品
<img src="img/parts_roller_stopper_spacer.png" width="1600">

----


<img src="./img/2025-07-30-11-09-04.png" width="1600" class="popup-image">

<img src="./img/roller_stopper_spacer.png" width="100" class="popup-image">

<img src="./img/M2_15.png" width="100" class="popup-image">

---

車輪

<img src="./img/2025-07-30-12-18-33.png" width="600" class="popup-image">

<img src="./img/2025-07-30-17-11-37.png" width="600" class="popup-image">

----

サーボ

<img src="./img/2025-07-30-17-12-29.png" width="600" class="popup-image">

羽を削る
<img src="./img/2025-08-23-10-09-30.png" width="600" class="popup-image">
<img src="./img/2025-08-22-20-44-59.png" width="600" class="popup-image">


前輪とサーボ

<img src="./img/2025-08-21-11-15-00.png" width="600" class="popup-image">

<img src="./img/2025-08-21-11-16-34.png" width="600" class="popup-image">

配線の入れ替え
<img src="./img/2025-08-02-12-27-51.png" width="600" class="popup-image">

シャーシに嵌め込む
<img src="./img/2025-07-30-12-42-32.png" width="600" class="popup-image">

----

モーター 後輪

<img src="./img/2025-07-30-17-09-14.png" width="1600" class="popup-image">

<img src="./img/2025-07-30-17-13-12.png" width="1600" class="popup-image">

横上から滑り入れる

<img src="./img/2025-07-30-18-02-54.png" width="400" class="popup-image">

<img src="./img/2025-07-30-18-45-08.png" width="600" class="popup-image">

<img src="./img/2025-07-30-18-53-19.png" width="600" class="popup-image">

<img src="./img/2025-07-30-19-23-33.png" width="600" class="popup-image">


----

カメラ（前）バッテリーのホルダー（後ろ）

<img src="./img/2025-07-30-19-21-57.png" width="600" class="popup-image">

<img src="./img/M2_10.png" width="600" class="popup-image">

<img src="./img/2025-07-30-19-49-41.png" width="600" class="popup-image">

<img src="./img/2025-07-30-20-03-35.png" width="600" class="popup-image">

----

配線

<img src="./img/2025-07-30-20-15-43.png" width="1600" class="popup-image">

<img src="./img/2025-07-30-20-14-33.png" width="600" class="popup-image">

<img src="./img/2025-07-30-20-26-04.png" width="600" class="popup-image">

ハンダつけ

<img src="./img/2025-08-02-10-56-24.png" width="1600" class="popup-image">

ピン位置

https://github.com/covao/TatamiRacer/blob/master/img/TatamiRacer_Circuit.png

<img src="./img/2025-08-23-10-14-02.png" width="1600" class="popup-image">


---


## Donkey SW セットアップ

  https://docs.donkeycar.com/guide/robot_sbc/setup_raspberry_pi/

Donkeyバージョン 4.5のRaspi Busterなので 「Installation for Donkeycar <= 4.5 using Raspberry Pi OS Buster」のセクションに従ってください。

### Step 1 - 5

Raspi imager

{{<img src="./img/2025-08-10-14-51-34.png" width="600" class="popup-image">}}

- General

  {{<img src="./img/2025-08-10-14-53-42.png" width="600" class="popup-image">}}

  - hostname: tatamiracer-zero.local
  - username: pi
  - wifi SSID: Your WiFi (2.4GHz)

- Enable SSH : don't make it true

  put `ssh` empty file in boot/ directory of the sd card

  {{<img src="./img/2025-08-10-14-52-53.png" width="600" class="popup-image">}}


  ```
  ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no pi@192.168.68.50
  ```

ミニ HDMI ( micro < mini < normal) でモニターをつける場合

config.txt

  Before
  ```
  #hdmi_safe=1
  #framebuffer_width=1280
  #framebuffer_height=720
  dtoverlay=vc4-kms-v3d
  ```

  After
  ```
  hdmi_safe=1
  framebuffer_width=1280
  framebuffer_height=720
  #dtoverlay=vc4-kms-v3d
  ```

  うまくいかない場合は 以下も試してみてください

  ```
  hdmi_force_hotplug=1
  hdmi_group=2
  hdmi_mode=51

  [all]
  dtoverlay=vc4-fkms-v3d
  #dtoverlay=vc4-kms-v3d,nocomposite
  #dtoverlay=ov5647
  dtoverlay=imx219
  ```


### WiFi 設定

 wpa_supplicant.conf

 ```
 country=JP
  ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
  update_config=1
  network={
      ssid="BIRDS Coworking×FUKUROI"
      psk="xxxxx"
  }
  ```


- [step6](https://docs.donkeycar.com/guide/robot_sbc/setup_raspberry_pi/#step-6-update-and-upgrade)

  ```
  sudo apt-get update --allow-releaseinfo-change
  sudo apt-get upgrade
  ```

  ```
  sudo raspi-config
  ```
  - i2c
  - camera
  - expand filesystem

- Step 7

- Step 8

  ```
  sudo apt-get install build-essential python3 python3-dev python3-pip python3-virtualenv python3-numpy python3-picamera python3-pandas python3-rpi.gpio i2c-tools avahi-utils joystick libopenjp2-7-dev libtiff5-dev gfortran libatlas-base-dev libopenblas-dev libhdf5-serial-dev libgeos-dev git ntp
  ```

- Step 9
- Step 10

  ```
  python3 -m virtualenv -p python3 env --system-site-packages
  echo "source ~/env/bin/activate" >> ~/.bashrc
  source ~/.bashrc
  ```

- Step 11

  ```
  mkdir projects
  cd projects

  git clone https://github.com/autorope/donkeycar
  cd donkeycar
  git fetch --all --tags -f
  git checkout 4.5.1
  ```

  ⭐️Install opencv-python しておく

  ```
  pip install opencv-python==4.5.1.48

  ```

  ```
  pip install -e .[pi]
  pip install https://github.com/lhelontra/tensorflow-on-arm/releases/download/v2.2.0/tensorflow-2.2.0-cp37-none-linux_armv7l.whl
  ```

  - Check tensorflow version

    ```
    python -c "import tensorflow; print(tensorflow.__version__)"
    ```

  - Fix

    ```
    pip install protobuf==3.20.1
    ```

---

## TatamiRacer の設定手順

https://github.com/covao/TatamiRacer/blob/master/doc/HowToSetupSoftware.md#install-donkey-car-application-for-raspberry-pi

### VNC

```
sudo apt install realvnc-vnc-server realvnc-vnc-viewer
sudo raspi-config nonint do_vnc 0
```

  - https://www.freva.com/how-to-fix-cannot-currently-show-the-desktop-on-raspberry-pi/

  ```
  echo 'hdmi_force_hotplug=1'>> /boot/config.txt
  echo 'hdmi_group=2'>> /boot/config.txt
  echo 'hdmi_mode=51'>> /boot/config.txt
  ```


  ```
  sudo apt install xserver-xorg lightdm lxde-core lxterminal
  ```

## Create mycar

```
donkey createcar --path ~/mycar
```

[Setup TatamiRacer by Shell Script](https://github.com/covao/TatamiRacer/blob/master/doc/HowToSetupSoftware.md#setup-tatamiracer-by-shell-script)

```
wget "https://raw.githubusercontent.com/covao/TatamiRacer/master/raspi/install/setup_tatamiracer.sh" -O "setup_tatamiracer.sh"
sh -x setup_tatamiracer.sh
```

### ラズパイZeroのIPアドレスの見つけ方

ローカルPCで arpコマンドを利用

> donkey findcarは 2c:cfを見ていない

```
arp -a | grep 2c:cf
```

### camera


- raspistill

  ```
  vcgencmd get_camera

  sudo raspistill -o image.jpg
  ```

- raspivid

- libcamera-hello

```
sudo apt install libcamera-apps
```

https://zenn.dev/kobayutapon/articles/490d93ab683337

- V1 camera (OV5647)	dtoverlay=ov5647
- V2 camera (IMX219)	dtoverlay=imx219

```
sudo raspi-config nonint do_legacy 0
```


## Setup TatamiRacer by Shell Script

```
wget "https://raw.githubusercontent.com/covao/TatamiRacer/master/raspi/install/setup_tatamiracer.sh" -O "setup_tatamiracer.sh"
sh -x setup_tatamiracer.sh
```


bullseysの
[Raspberry Pi Zero2 Wでカメラ・OpenCV環境を整える](https://zenn.dev/kobayutapon/articles/490d93ab683337)

---

## TatamiRacerのDonkey 4.5対応 ⭐️

 https://github.com/KwikHangout/AI-RC/tree/main/src/mycar_tatamiracer


---

## カリブレーション

  tatamiracer_test.pyを利用して、myconfig.pyの値を後進　⭐️

  うまくいかない場合は 配線やGPIOデーモンを確認

  ```
  sudo systemctl restart pigpiod
  ```
---

## 走行

myconfig.py

```
CONTROLLER_TYPE = 'F710'
```

python manage.py drive --js

---

## PCでトレーニング

get data

```
rsync -rv --progress --partial pi@tatamiracer-zero:~/mycar/data/  ./data/
```

train
```
~\mycar$ donkey train --tub ./data --model ./models/mypilot.h5
```

copy back
```
rsync -rv --progress --partial ./models/ pi@tatamiracer-zero:~/mycar/models/
```

auto pilot

```
python manage.py drive --js --model ./models/mypilot.tflite --type tflite_linear
```


-----

参考

**Control Logic (Python using RPi.GPIO for one DC Motor):**

To control the DC motor's direction and speed using the MX1508, you'll manipulate the IN1 and IN2 pins. For speed control, you'll apply PWM to one of the input pins.

```python
import RPi.GPIO as GPIO
from time import sleep

# --- MX1508 (DC Motor) setup ---
# GPIO pin assignments (BCM mode, adjust as needed)
MOTOR_IN1 = 17 # Connect to IN1 on MX1508
MOTOR_IN2 = 18 # Connect to IN2 on MX1508

GPIO.setmode(GPIO.BCM)
GPIO.setup([MOTOR_IN1, MOTOR_IN2], GPIO.OUT)

# For speed control, we'll apply PWM to one of the pins
# For example, to go forward, set IN1 HIGH and apply PWM to IN2 (or vice-versa, depending on desired direction)
# Let's assume applying PWM to IN2 for forward, and IN1 for backward.
PWM_PIN_FOR_SPEED = MOTOR_IN2 # For forward direction
# You might want a dedicated PWM instance if controlling both directions with speed
# Or handle PWM logic within the functions

# Setting up a single PWM instance for one of the IN pins for simplicity in speed control example
# Note: You can also implement software PWM by rapidly toggling the pins, or use hardware PWM if available on your chosen pins.
# For simplicity, we'll use a single PWM for one direction here.
# For the MX1508, typically you hold one INx low and apply PWM to the other INx to control speed.
# Let's set up a PWM on MOTOR_IN2 for forward movement speed.
pwm_motor_speed = GPIO.PWM(PWM_PIN_FOR_SPEED, 100) # 100 Hz frequency
pwm_motor_speed.start(0) # Start with 0% duty cycle (motor off)

def motor_forward(speed):
    """
    Drives the motor forward at a given speed (0-100).
    Here, IN1 is HIGH, IN2 receives PWM.
    """
    GPIO.output(MOTOR_IN1, GPIO.HIGH)
    # The speed is controlled by the duty cycle of IN2
    pwm_motor_speed.ChangeDutyCycle(speed)
    print(f"Motor Forward at {speed}% speed")

def motor_backward(speed):
    """
    Drives the motor backward at a given speed (0-100).
    Here, IN2 is HIGH, IN1 receives PWM.
    NOTE: You would need to reconfigure pwm_motor_speed to MOTOR_IN1 for this to work directly as coded.
    A more robust solution involves toggling the PWM pin or managing two PWM instances.
    For simplicity here, let's just reverse the HIGH/LOW and skip direct PWM on backward for this example.
    To control speed backward, you'd apply PWM to MOTOR_IN1 and keep MOTOR_IN2 HIGH.
    A simpler approach for MX1508 is often just direct digital control for direction, and applying PWM
    to the "active" input.
    Let's refine this to be more common for MX1508:
    """
    GPIO.output(MOTOR_IN2, GPIO.HIGH)
    # To control backward speed, you'd apply PWM to MOTOR_IN1.
    # For this example, let's just set MOTOR_IN1 to a fixed state for direction, no speed control on backward.
    # To properly control speed in both directions with a single PWM instance, you'd need more complex logic
    # or control the PWM duty cycle after setting the direction.
    GPIO.output(MOTOR_IN1, GPIO.LOW) # For fixed backward
    # To control speed backward, you'd actually want something like:
    # pwm_motor_speed.ChangeFrequency(100) # Ensure frequency is set
    # pwm_motor_speed.ChangeDutyCycle(0) # Stop current PWM
    # GPIO.output(MOTOR_IN1, GPIO.LOW) # Set direction
    # GPIO.output(MOTOR_IN2, GPIO.HIGH)
    # pwm_motor_speed.ChangeDutyCycle(speed) # Apply PWM to the correct pin

    # Let's redefine for common MX1508 PWM usage:
    # One pin is HIGH/LOW, the other is PWM.
    # If IN1=HIGH, IN2=PWM_DUTY_CYCLE -> Motor A in one direction, speed controlled by PWM
    # If IN1=PWM_DUTY_CYCLE, IN2=HIGH -> Motor A in other direction, speed controlled by PWM

    # For now, let's simplify to direct control with full speed for backward.
    GPIO.output(MOTOR_IN1, GPIO.LOW)
    GPIO.output(MOTOR_IN2, GPIO.HIGH)
    pwm_motor_speed.ChangeDutyCycle(speed) # If PWM_PIN_FOR_SPEED is IN2, this will still be forward.
                                         # A single PWM is tricky for both directions this way.
                                         # Let's adjust the simple example to only show forward speed.

    print(f"Motor Backward at {speed}% speed (Note: Speed control might be simplified here)")
    # For robust speed control in both directions with MX1508, you usually:
    # 1. Set one IN pin LOW, the other IN pin to PWM.
    # 2. To reverse, set the first IN pin to PWM, the other IN pin LOW.
    # The RPi.GPIO PWM instance is tied to a specific pin.
    # So, you would likely need to stop/start PWM on different pins, or use a library that abstracts this.

    # Simpler approach: set direction, then apply PWM
    # For forward: IN1=HIGH, IN2=PWM(speed)
    # For backward: IN1=PWM(speed), IN2=HIGH
    # This requires dynamically managing which pin the PWM instance is on, or having two PWM instances.

    # Let's revise the functions to handle speed control more realistically for MX1508:
    # We will use one PWM instance and switch which pin is high/low.

def set_motor_speed_and_direction(direction, speed):
    """
    Controls the motor direction and speed (0-100).
    direction: 'forward', 'backward', 'stop'
    """
    if direction == 'forward':
        GPIO.output(MOTOR_IN1, GPIO.HIGH)
        # Apply PWM to IN2 for forward speed
        # Ensure pwm_motor_speed is managing IN2. This is the tricky part with a single PWM object.
        # A more direct way is to set duty cycle and then set the other pin.
        GPIO.output(MOTOR_IN2, GPIO.LOW) # Set IN2 low initially
        # Then, apply PWM to IN2 by toggling it or dynamically changing PWM source
        # For simplicity, we'll use a direct digital approach if no hardware PWM is on *both* pins needed.

        # Let's use software PWM or just simple on/off for basic example given the MX1508.
        # If speed control is needed, you set one pin high and apply PWM to the other.
        # This typically means pwm_motor_speed needs to be associated with MOTOR_IN2 for forward.
        # And if going backward, it needs to be associated with MOTOR_IN1.
        # This implies changing the PWM pin, or having two PWM instances, or managing a single one carefully.

        # For this example, let's just do simple direction control first, then add basic speed later.
        GPIO.output(MOTOR_IN1, GPIO.HIGH)
        GPIO.output(MOTOR_IN2, GPIO.LOW)
        if speed > 0:
            # Simple speed control: cycle between ON/OFF based on speed
            # This is not RPi.GPIO.PWM, but a conceptual software PWM
            # For actual PWM, you'd use pwm_motor_speed.ChangeDutyCycle(speed)
            # but you'd need to ensure pwm_motor_speed is applied to the correct pin.
            # Let's assume you've set pwm_motor_speed on MOTOR_IN2, for forward.
            # And for backward, you'd set it on MOTOR_IN1. This needs re-initialization.

            # Easiest way for MX1508 with speed:
            # Define two PWM objects if you want fine control in both directions
            # OR, use a single PWM object on a specific pin and set the other pin HIGH/LOW
            # and only control speed when that PWM pin is the active one.

            # Revert to the basic on/off and then explain PWM nuance.
            # Basic digital control for MX1508:
            # IN1 | IN2 | Motor Action
            # --- | --- | ------------
            # LOW | LOW | Stop
            # HIGH| LOW | Forward
            # LOW | HIGH| Reverse
            # PWM | LOW | Forward (Speed controlled by PWM)
            # LOW | PWM | Reverse (Speed controlled by PWM)

            # Given this, let's redefine the motor control functions without a global pwm_motor_speed.
            # We will use RPi.GPIO.PWM directly within the functions, or assume a fixed PWM pin.
            # The most flexible way: Use a function that takes 'pin_to_pwm' and 'pin_to_set_low'.
            # But that requires passing the PWM object.

            # Let's use a clear, basic approach for controlling direction, and then integrate a single PWM for one direction.
            # For real bidirectional speed, use pigpio or a more advanced library.

            # Simple forward with speed (PWM on IN2)
            pwm_motor_forward = GPIO.PWM(MOTOR_IN2, 100) # PWM on IN2
            pwm_motor_forward.start(0)
            GPIO.output(MOTOR_IN1, GPIO.HIGH) # Set IN1 high
            pwm_motor_forward.ChangeDutyCycle(speed)
            print(f"Motor Forward at {speed}% speed (PWM on IN2)")
            return pwm_motor_forward # Return PWM object to stop later

    elif direction == 'backward':
        # Simple backward with speed (PWM on IN1)
        pwm_motor_backward = GPIO.PWM(MOTOR_IN1, 100) # PWM on IN1
        pwm_motor_backward.start(0)
        GPIO.output(MOTOR_IN2, GPIO.HIGH) # Set IN2 high
        pwm_motor_backward.ChangeDutyCycle(speed)
        print(f"Motor Backward at {speed}% speed (PWM on IN1)")
        return pwm_motor_backward # Return PWM object to stop later

    elif direction == 'stop':
        GPIO.output(MOTOR_IN1, GPIO.LOW)
        GPIO.output(MOTOR_IN2, GPIO.LOW)
        print("Motor Stopped")
        return None # No PWM object to return

try:
    print("Motor Forward at 70% speed...")
    current_pwm = set_motor_speed_and_direction('forward', 70)
    sleep(2)
    if current_pwm: current_pwm.stop() # Stop previous PWM

    print("Motor Backward at 50% speed...")
    current_pwm = set_motor_speed_and_direction('backward', 50)
    sleep(2)
    if current_pwm: current_pwm.stop() # Stop previous PWM

    set_motor_speed_and_direction('stop', 0)
    sleep(1)

except KeyboardInterrupt:
    pass
finally:
    # Ensure all GPIO pins are set to LOW and cleaned up
    GPIO.output(MOTOR_IN1, GPIO.LOW)
    GPIO.output(MOTOR_IN2, GPIO.LOW)
    GPIO.cleanup()
    print("GPIO cleanup complete.")
```

**Important Notes for MX1508:**

  * **PWM for Speed:** For the MX1508, to control speed, you typically keep one INx pin HIGH and apply a PWM signal to the other INx pin for that motor. Reversing direction then involves switching which pin receives the PWM and which is held HIGH. The `RPi.GPIO.PWM` object is tied to a specific pin. For bidirectional speed control, you might need to create and stop/start `PWM` objects on different pins, or use a library like `pigpio` which offers more flexible software PWM across all GPIOs. The example above illustrates how to start a new PWM for each direction for clarity.
  * **Voltage:** Ensure your external power supply's voltage matches your DC motor's rated voltage and is within the MX1508's operating range (typically 2V-10V).
  * **Current:** The MX1508 is suitable for small motors. If your DC motor draws significant current (over 1.5A continuous), this module might not be sufficient, and you would need a more powerful driver.
  * **Common Ground:** Always connect the GND of your external motor power supply to a GND pin on your Raspberry Pi.

This setup should allow you to control your DC motors with the MX1508 driver from your Raspberry Pi. Remember to adjust the GPIO pin numbers in the code to match your actual wiring.
