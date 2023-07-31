donkey-kwiksher - raspi3 - update 2023 Jul 28
  - 4.5.0
  - tensorflow 2.3.0

  ```
  sudo apt-get update --allow-releaseinfo-change
  sudo apt-get upgrade

  pip install https://github.com/lhelontra/tensorflow-on-arm/releases/download/v2.3.0/tensorflow-2.3.0-cp37-none-linux_armv7l.whl

  python -c "import tensorflow; print(tensorflow.__version__)"
  python -c "import numpy; print(numpy.version.version)"
  python -c "import cv2; print(cv2.__version__)"
  ```

 - opencv

  pip install opencv-python==4.5.1.48

  - mysim

  ```
    pip install gym
    git clone https://github.com/tawnkramer/gym-donkeycar
    cp gym-donkeycar/gym-donkeycar ./mysim/
  ```

raspi 4
	vnc viewerでアクセスする

	scan disk     raspoberrypi.local
		solar2D

	scan disk pro surrogete-rpi.local for Mobile Mover
		mavproxy
		joystick
		suroogete

    pi/create1337


	scan disk pro surrogate-kwiksher.local
		donkey
		OBS
		surrogate

    pi/creator1337


   - lsb_release -a

      ```
      No LSB modules are available.
      Distributor ID: Raspbian
      Description:    Raspbian GNU/Linux 10 (buster)
      Release:        10
      Codename:       buster
      ```

  For raspi4 buster

  - https://docs.donkeycar.com/guide/robot_sbc/setup_raspberry_pi/#step-1-flash-operating-system

    - Step 6: Update and Upgrade

      ```
      sudo apt-get update --allow-releaseinfo-change
      sudo apt-get upgrade
      ```
    - Step 11:

      ```
      git fetch --all --tags -f
      latestTag=$(git describe --tags `git rev-list --tags --max-count=1`)
      git checkout $latestTag
      pip install -e .[pi]
      ```

      > opencv-python is not finished

      https://raspberrypi-guide.github.io/programming/install-opencv

      ```
      pip install opencv-python==4.8.0.74
      sudo apt-get install python-opencv
      ```
    - Camera

      ```
      vcgencmd get_camera
      raspistill -o test.jpg
      ```

      [Raspberry Piでカメラが認識しない際の対処法](https://qiita.com/kaiyu0401/items/0d27ec359b5a692c1f89)

      ```
      sudo rpi-update
      ```

      - failed to open vchiq instance

        https://gokids.hatenablog.com/entry/2018/10/23/200000
        http://blawat2015.no-ip.com/~mieki256/diary/201708304.html

        ```
        sudo chmod 777 /dev/vchiq
        ```
   - i2c

      [Errno 2] No such file or directory: '/dev/i2c-1'

   - My Virtual Donkey

      https://docs.donkeycar.com/guide/deep_learning/simulator/

      ```
      pip install gym==0.21
      ```
      > pip install gym will install 0.26

  - tensorflow 2.3.1 to work with jetson nano

  pip install https://github.com/lhelontra/tensorflow-on-arm/releases/download/v2.3.0/tensorflow-2.3.0-cp37-none-linux_armv7l.whl

    this requires numpy > 1.19
  =>
     not work

     back to 2.2.0

    ```
    pip install https://github.com/lhelontra/tensorflow-on-arm/releases/download/v2.2.0/tensorflow-2.2.0-cp37-none-linux_armv7l.whl
    ```

------
mac headless raspi
    cmdline.txt

        console=serial0,115200 console=tty1 root=PARTUUID=3916cabe-02 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait modules-load=dwc2,g_ether quiet splash plymouth.ignore-serial-consoles

    config.txt
        dtoverlay=dwc2

find ip addresssur

    arp -a
    nmap -sP 192.168.0.0/24

    ----------
    windows では nmap, awkをインストール して donkey findcarが動く

    management/base.py のnmapの部分をちょこっと修正 sudo と文字エスケープ

            cmd = "nmap -sP " + ip + "/24 | awk " + '"/^Nmap/{ip=$NF}/B8:27:EB/{print ip}"'
    ----------------------------


GUIをインストール - raspi4

    https://walking-succession-falls.com/%E3%83%A9%E3%82%BA%E3%83%99%E3%83%AA%E3%83%BC%E3%83%91%E3%82%A4%E3%81%ABGUI%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B

sudo raspi-config

    enable VNC
    - Interface > VNC
    - Boot Option > Desktop GUI, requiring user to login
    - Display Options > D1 Resolution > DMT Mode 85 1280×720

GL driver

  - enable FKMS


OBS studio

    sudo apt-get install software-properties-common
    sudo apt install ffmpeg
    sudo apt install v4l2loopback-dkms
    sudo add-apt-repository ppa:obsproject/obs-studio
    sudo apt update
    sudo apt install obs-studio

    https://raspberrytips.com/install-obs-studio-raspberry-pi/

    ```
    sudo apt install build-essential checkinstall cmake git libmbedtls-dev libasound2-dev libavcodec-dev libavdevice-dev libavfilter-dev libavformat-dev libavutil-dev libcurl4-openssl-dev libfontconfig1-dev libfreetype6-dev libgl1-mesa-dev libjack-jackd2-dev libjansson-dev libluajit-5.1-dev libpulse-dev libqt5x11extras5-dev libspeexdsp-dev libswresample-dev libswscale-dev libudev-dev libv4l-dev libvlc-dev libx11-dev libx11-xcb1 libx11-xcb-dev libxcb-xinput0 libxcb-xinput-dev libxcb-randr0 libxcb-randr0-dev libxcb-xfixes0 libxcb-xfixes0-dev libx264-dev libxcb-shm0-dev libxcb-xinerama0-dev libxcomposite-dev libxinerama-dev pkg-config python3-dev qtbase5-dev libqt5svg5-dev swig

    sudo apt install qtbase5-private-dev

    wget http://ftp.debian.org/debian/pool/non-free/f/fdk-aac/libfdk-aac2_2.0.1-1_armhf.deb
    wget http://ftp.debian.org/debian/pool/non-free/f/fdk-aac/libfdk-aac-dev_2.0.1-1_armhf.deb

    sudo dpkg -i libfdk-aac2_2.0.1-1_armhf.deb
    sudo dpkg -i libfdk-aac-dev_2.0.1-1_armhf.deb

    sudo git clone --recursive https://github.com/obsproject/obs-studio.git
    cd obs-studio

    sudo mkdir build
    cd build

    sudo cmake -DBUILD_BROWSER=OFF -DENABLE_WAYLAND=OFF -DENABLE_PIPEWIRE=OFF -DUNIX_STRUCTURE=1 -DCMAKE_INSTALL_PREFIX=/usr ..

    sudo make -j4

    sudo make install

    sudo MESA_GL_VERSION_OVERRIDE=3.3 obs

camera

    ```
    lsusb

    ls /dev/video*

    sudo apt-get install guvcview

    ```

swap
    ```
    vi /etc/dphys-swapfile
        CONF_SWAPSIZE=1024

    sudo systemctl stop dphys-swapfile
    sudo systemctl start dphys-swapfile

    swapon -s
    ```


donkey-kwiksher
    passwd:donkey


    http://blog.1q77.com/2012/12/tool-for-enabling-and-disabling-wireless-devices/
    sudorfkill unblock wifi
    sudo ifconfig wlan0 up


    donkey    3.7.3
    surrogate 3.7.8

    https://github.com/SurrogateInc/surrortg-sdk

    - pyenv

        ```
        sudo apt-get update && sudo apt-get upgrade && sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
        ```

        ```
        curl https://pyenv.run | bash
        ```

        nano ~/.bashrc
        ```
        export PATH="/home/$USER/.pyenv/bin:$PATH"
        eval "$(pyenv init -)"
        eval "$(pyenv virtualenv-init -)"
        ```

        ```
        cd surrortg-sdk
        pyenv install 3.7.8
        pyenv local 3.7.8
        ```

        surrortg dependencies

        ```
        pip install pipenv
        pipenv sync
        pipenv shell
        ```

    https://docs.surrogate.tv/getting_started.html#sdk-installation


- Coral USB tpu

  https://docs.donkeycar.com/parts/stop_sign_detection/
  https://coral.ai/docs/accelerator/get-started#3-run-a-model-on-the-edge-tpu


WiFi
  Wifiつながらない時は
  チピファイつかうって手も
  https://faboplatform.github.io/DonkeyDocs/4.etc/1.wifi/
  こんな感じで固定IP割り振られます

  https://faboplatform.github.io/DonkeyDocs/4.etc/3.joystick/
  Joystick Hack完了
  これで、どのJoystickでも対応可能に

  https://github.com/FaBoPlatform/donkeypart_ps3_controller

Ishinomaki

    sudo bluetoothctl
    connect 78:D2:00:6C:57:54

    # 一旦デーモンをkillしてみる
    pulseaudio -k

    # 再度スタート
    pulseaudio -k
    pulseaudio --start

    # rootをpulse-accessグループに追加
    sudo gpasswd -a root pulse-access

    sudo aplay open_jtalk.wav

    sudo shutdown -h now

    sudo reboot

---
[raspberry pi3 で bluetooth スピーカーに接続する](https://qiita.com/Sam/items/5169d9f060aa31080b77)a

  sudo apt install pulseaudio pulseaudio-module-bluetooth
  sudo apt-get install pavucontrol

  sudo pip install netifaces

  ymmtny
  ssh pi@192.168.10.21

  white donkey
  ssh pi@192.168.10.18
  python manage.py drive --j &
  pkill -f manage.py

  tensorboard          1.13.1
  tensorflow           1.13.1

  ssh pi@192.168.43.225

  conda activate donkey
  python manage.py drive --j

  sudo raspi-config
      change default password for pi
      change hostname
      enable Interfacing Options | I2C
      enable Interfacing Options | Camera
      Advanced Options | Exapand Filesystem

  ls /dev/input/js0

  rsync -r pi@donkey-kwiksher.local:~/Donkey/mycar/data/ ./mycar/data/

  Open Terminal.app // train failed with VS Code Integareted terminal

  cd ./data
  donkey tubclean ./

  python manage.py train --tub ./data/tub_15_19-08-02 --model ./models/mypilot.h5

  python manage.py drive --model ./models/mypilot.h5

- numpy

  - 1.19.0