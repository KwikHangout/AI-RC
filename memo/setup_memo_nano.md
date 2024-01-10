- ubuntu 20.04 image

  - https://github.com/Qengineering/Jetson-Nano-Ubuntu-20-image
  - https://my-cluttered-blog.com/it_techronolgy/74/

    - software keyboard
    - ssh enabeld
    - expand it for 64GB sd card

  ```
  sudo apt-get install ssh
  sudo apt-get install gparted
  ```

  ```
  pip3 install virtualenv
  python3 -m virtualenv -p python3 env --system-site-packages
  echo "source ~/env/bin/activate" >> ~/.bashrc
  source ~/.bashrc
  ```

  skipping Setup Python Dependencies in https://docs.donkeycar.com/guide/robot_sbc/setup_jetson_nano/


  ```
  mkdir projects
  cd ~/projects
  git clone https://github.com/autorope/donkeycar
  cd donkeycar
  git fetch --all --tags -f
  latestTag=$(git describe --tags `git rev-list --tags --max-count=1`)
  git checkout $latestTag
  ```

  instead of [nano45] use [pc]

  ```
  export MAKEFLAGS="-j4"
  pip install -e .[pc]
  ```
  15:12
  15:58 error
    ```
    pip install opencv-python

      Successfully installed numpy-1.24.4 opencv-python-4.8.0.74

      tensorflow 2.4.1 requires numpy~=1.19.2, but you have numpy 1.24.4 which is incompatible.

    https://pypi.org/project/opencv-python-headless/4.4.0.46/#files

    python3 -m pip install ./opencv-python-headless-4.4.0.46.tar.gz
    ```

  https://discuss.tensorflow.org/t/tensorflow-and-numpy-issue/6238

  ```
  pip install opencv-python==4.6.0.66
  pip install opencv-python-headless==4.6.0.66
  pip install numpy==1.19.5
  ```

  16:48
  17:26 error

  17:33 ⭐️ let's install opencv-python-headless-4.6.0.66

  ```
  cd projects

  wget https://files.pythonhosted.org/packages/fe/5d/f99eb2182c6f7bf9647babe6f86f5e397f6be07a2035bbdf272e7cb16cd4/opencv-python-headless-4.6.0.66.tar.gz

  tar xvzf opencv-python-headless-4.6.0.66.tar.gz

  #fix cmake_install_dir with _cmake_install_dir in setup.py

  pip install opencv-python-headless-4.6.0.66
  ```

  pip install -e.[pc] --find-links=../


  ```
  ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
  opencv-python 4.6.0.66 requires numpy>=1.19.3; python_version >= "3.6" and platform_system == "Linux" and platform_machine == "aarch64", but you have numpy 1.19.0 which is incompatible.
  tensorflow 2.4.1 requires numpy~=1.19.2, but you have numpy 1.19.0 which is incompatible.
  Successfully installed Kivy-Garden-0.1.5 PrettyTable-3.8.0 PyWavelets-1.4.1 albumentations-1.3.1 docopt-0.6.2 docutils-0.20.1 donkeycar imageio-2.31.1 joblib-1.3.1 kivy-2.2.1 networkx-3.1 numpy-1.19.0 paho-mqtt-1.6.1 plotly-5.15.0 progress-1.6 psutil-5.9.5 pyfiglet-0.8.post1 pygments-2.15.1 pynmea2-1.19.0 qudida-0.0.4 scikit-image-0.19.3 scikit-learn-1.3.0 scipy-1.9.3 simple_pid-2.0.0 tenacity-8.2.2 threadpoolctl-3.2.0 tifffile-2023.7.10 tornado-6.3.2 utm-0.7.0
  ```

 - skimage error

  ImportError: /home/jetson/env/lib/python3.8/site-packages/skimage/_shared/../../scikit_image.libs/libgomp-d22c30c5.so.1.0.0: cannot allocate memory in static TLS block
  It seems that scikit-image has not been built correctly.

  ```
  wget https://files.pythonhosted.org/packages/00/d4/6682033d02917b10a2024dbe5a0636d2338b0799f7bd1885508fb114aec9/scikit-image-0.19.3.tar.gz
  ```

  export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgomp.so.1:/home/jetson/env/lib/python3.8/site-packages/scikit_image.libs/libgomp-d22c30c5.so.1.0.0


  pip install -U typing_extensions

  ```
  ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
  tensorflow 2.4.1 requires numpy~=1.19.2, but you have numpy 1.19.0 which is incompatible.
  tensorflow 2.4.1 requires typing-extensions~=3.7.4, but you have typing-extensions 4.7.1 which is incompatible.
  Successfully installed typing_extensions-4.7.1
  ```

  - train

   batch size 8
   ```
    2023-07-31 14:37:33.976924: E tensorflow/core/platform/default/subprocess.cc:212] Start cannot fork() child process: Cannot allocate memory

    Epoch 00014: val_loss did not improve from 0.00493
    Unable to init server: Could not connect: Connection refused
    Unable to init server: Could not connect: Connection refused

    (donkey:15930): Gdk-CRITICAL **: 14:39:32.371: gdk_cursor_new_for_display: assertion 'GDK_IS_DISPLAY (display)' failed
    INFO:donkeycar.parts.interpreter:Convert model /home/jetson/projects/mysim/models/mypilot.h5 to TFLite /home/jetson/projects/mysim/models/mypilot.tflite
   ```

    batch size 4

----

- rsync

  rsync -rv --progress --partial ./mysim_raspi/data/ jetson@nano-kwiksher.local:~/projects/mysim/data/


- traiining

  ps -aux | grep "donkey"

  ls -1 ./data/images | wc -l.

  donkey train --tub ./data --model ./models/mypilot.h5

  - error

  ```
   cannot allocate memory in static TLS block
    ```

    export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgomp.so.1

- drive

  python manage.py drive --model ./models/pilot_23-07-28_0.tflite --type tflite_linear

  python manage.py drive --model ./models/mypilot.tflite --type tflite_linear

  - gym

    git clone https://github.com/tawnkramer/gym-donkeycar

    it seems all right to ignore this error
    ```
    module 'setuptools.build_meta' has no attribute '__legacy__'
    ```

- aufumentations ⭐️

  > comment out the following line or build it with opencv-python-headless-4.4.0.46

  https://github.com/autorope/donkeycar/issues/1136
  ```
  donkeycar/donkeycar/pipeline/augmentations.py

    Line 13 in 1398eec

    class ImageAugmentation:
    . with ones based on opencv so we can remove albumentations.
  ```

 pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v45 tensorflow==2.3.1

 pip install numpy==1.19

 pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v45 tensorflow==2.5.0



----

https://opencv-python-headless-4.6.0.66/guide/robot_sbc/setup_jetson_nano/

```
cat /etc/issue
sudo apt-cache show nvidia-jetpack
free -h
df -k
python -c 'import tensorflow as tf; print(tf.__version__)'
python -c "import numpy; print(numpy.version.version)"
python -c "import cv2; print(cv2.__version__)"

```
=>

    buntu 18.04.6 LTS \n \l

    Package: nvidia-jetpack
    Version: 4.5.1-b17

- h5py error

  https://forums.developer.nvidia.com/t/h5py-build-failing-during-tensorflow-install/174002/3

  ```
  sudo apt-get install python3-pip
  sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev
  pip3 install cython
  pip3 install h5py==2.10.0
  ```
  => error
    h5py/_conv.pyx:860:12: 'H5PY_OBJ' is not a constant, variable or function identifier

  https://stackoverflow.com/questions/74798874/nano-jetson-jetpack-¡4-6-1-cant-install-right-h5py-version

  =>
    tensorflow-2.7

    https://github.com/h5py/h5py/issues/1533

    ```
    pip install cython==0.29
    ```

    https://github.com/pypa/setuptools/issues/1694

    ```
    pip install -e .[pc] --no-use-pep517
    ```

    https://bobbyhadz.com/blog/python-no-module-named-skbuild
    ```
    pip install scikit-build
    ```

    - ps command

      ```
      ps -eo lstart,pid,args | grep "pip install"
      ps -aux | grep "pip install"
      ```

      Sat Jul 29 17:05:35 2023 27375 /home/jetson/mypy36venv/bin/python3.6 /home/jetson/mypy36venv/bin/pip install -e .[pc] --no-use-pep517

      18:50
        File "/tmp/pip-install-3u605fah/opencv-python-headless_6903831b5a1a4dd3955510747fd4630c/setup.py", line 252, in main
        cmake_source_dir=cmake_source_dir,
       File "/home/jetson/mypy36venv/lib/python3.6/site-packages/skbuild/setuptools_wrap.py", line 683, in setup
        cmake_install_dir,
        File "/tmp/pip-install-3u605fah/opencv-python-headless_6903831b5a1a4dd3955510747fd4630c/setup.py", line 403, in _classify_installed_files_override
        cmake_install_dir=cmake_install_reldir,
        TypeError: _classify_installed_files() got an unexpected keyword argument 'cmake_install_dir'
        ----------------------------------------
        ERROR: Failed building wheel for opencv-python-headless

    =>
      ```
      pip install opencv-python
      ```

      not work. build the headless from the source

- opencv-python-headless 4.4.0.46

  pip install opencv-python-headless==4.4.0.46

  - https://pypi.org/project/opencv-python-headless/4.4.0.46/#files

    ```
    python3 -m pip install ./opencv-python-headless-4.4.0.46.tar.gz
    ```

  ~~pip install opencv-python==4.5.1.48~~
  ~~pip install opencv-python-headless==4.5.1.48~~

  https://qengineering.eu/install-opencv-on-jetson-nano.html

  https://albumentations.ai/docs/getting_started/installation/

  ```
  pip install -U albumentations --no-binary qudida,albumentations
  ```

  [OpenCV + OpenCV Contribをビルド 【Raspberry Pi OS編】](https://swallow-incubate.com/archives/blog/20200709/)

  Raspberry Pi 4 を信じてj4で行ってみます。所要時間は、筆者では約1時間

    |Raspberry Pi 4|Jetson Nano 2GB|
    |:------|:------|
    |4 core Cortex-A72@1.5GHz	|4 core A57@1.43 GHz|
    |Broadcom VideoCore VI	|128-core NVIDIA Maxwell™|
¡



- tensorflow==2.2.0

   > 4.5.0 on mac uses 2.2.0. Update it to 2.3.1 too or donwgrade it to 2.2.0

  - tensorflow==2.3.1

  ```
  pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v45 tensorflow==2.3.1
  ```

- python 3.6

```
sudo apt-get install python3.6
sudo apt-get install python3.6-venv
python3.6 -m venv mypy36venv --system-site-packages

source mypy36venv/bin/activate
python --version
```

ln -s /usr/include/locale.h /usr/include/xlocale.h


pip install wheel
pip install Cython

- release 4.5.0 does not have nano45 env. Use 'nano' instead of 'nano45'

  pip install -e .[nano]

- annoations

  https://stackoverflow.com/questions/66640159/use-annotations-on-pytnon-3-6-5

  git branch legacy_py3.6
  python setup.py install

- matplotlib

  https://discourse.odriverobotics.com/t/pip3-install-matplotlib-error-jetson-tx2-ubuntu-18-04/4248/6

  ```
  pip3 install -U pip
  pip3 install -U setuptools

  pip3 install matplotlib
  ```

- albumentations opencv-headless ⭐️

  https://forums.developer.nvidia.com/t/urgent-help-needed-need-to-install-on-headless-opencv-on-jetson-nano/141589/2