> 企画展の運営から借りたAsusノートブックのDonkey環境。英語キーボードです。

> jetson nanoドンキー1号機、２号機とも donkeycar 4.5.0 tensorflow 2.3.1です。これに合わせます。

## WSL Ubuntu

> UbuntuとUbuntu 22.04.3(バージョン付き) ２つが表示されていたら、バージョン名が無い方を選択してください。（重複して入れてしまったので、バージョン付きをアンインストールしましたが、残っているとこがあるみたいです）

## donkey carの環境

- [x] https://docs.donkeycar.com/guide/host_pc/setup_windows/

- [x] WSLとUbuntu
  - [x] vscode

    - user:donkey
    - password:!DonkeySkipCity2024

    remote explorerで入れます。

    <img src="./img/2024-01-13-10-51-31.png" width="600">

TODO

> 以下をお願いします。

- [ ] conda install python=3.6


    - [ ] https://docs.donkeycar.com/guide/host_pc/setup_ubuntu/

      > 現在のdonekycarのdocは 5.0.0用なので 3.9になってしまいます。


- [ ] opencv python headless

  ```
  sudo apt install python3-opencv
  pip install opencv-python==4.5.1.48
  ```

- [x] projectsフォルダ

  ```
  cd ~
  mkdir projects
  ```

- [ ] 4.5.0に変更

    https://docs.donkeycar.com/guide/host_pc/setup_ubuntu/

    - [x] tagsでチェックアウトしてください。ブランチ名 4.5.0

      ```
      git checkout tags/4.5.0 -b 4.5.0

      pip install -e .[pc]
      ```

  -  [ ] Cythonのバージョンエラーの対処

      setup.pyの修正

      ```
      Cython==0.29.36
      numpy==1.18.5

      'tf': ['tensorflow==2.3.1'],

      ```

      tf関連のインストールは、-e .[tf]

      ```
      pip install -e .[tf]
      ```

- [ ] 4.5.0に変更

    https://docs.donkeycar.com/guide/host_pc/setup_ubuntu/

    ```
    git checkout tags/4.5.0 -b 4.5.0

    pip install -e .[pc]
    conda update -n base -c defaults conda
    conda env remove -n donkey
  　
    donkey createcar --path ./mycar
    ```

 - [ ] 確認

    ```
    cat /etc/os-release

    python -c 'import tensorflow as tf; print(tf.__version__)'

    python -c "import cv2; print(cv2.__version__)"

    python -c "import numpy; print(numpy.version.version)"

    ```

----
## 学習をホストPCで実施

- [ ] ssh configの設定

  ```
  Host skipcity-donkey-01
    HostName 192.168.100.101
    User jetson

  Host skipcity-donkey-02
    HostName 192.168.100.102
    User jetson
  ```

ホストPCとrsync

1. **WiFiをDONKEY001に切り替える**

1. 以下のコマンドの実施

  ```
  cd /home/donkey/projects/mycar

  # 学習 dataの取得
  rsync -r jetson@skipcity-donkey-01o:~/mycar/data/ ./data/

  # 確認や学習の実施
  donkey ui

  # modelをドンキーカーに格納
  rsync -rv --progress --partial ./models/ jetson@skipcity-donkey-01:~/mycar/models/

  ```

  > donkey uiのcar connector の機能は動作しません rsyncを使ってください。
