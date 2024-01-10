- [ ] wltoys LiFe battery work?

- [ ] vnc in jetson nano? ubuntu with GUI?
- [ ] raspi3 with vs remote?

  - auto login by sudo raspi-config
  - ssh keys w/o password

    https://raspberrypi-guide.github.io/networking/connecting-via-ssh#passwordless-ssh

  - no password with ssh enable
    ```
    sudo passwd -d <username>
    PermitEmptyPasswords yes
    sudo service ssh restart
    ```

- [ ]  wifi with command line

  https://linuxconfig.org/ubuntu-20-04-connect-to-wifi-from-command-line


  ```
  $ ls /sys/class/net
  enp0s25  lo  wlp3s0

  $ ls /etc/netplan/

  $ sudoedit /etc/netplan/50-cloud-init.yaml

  $sudo netplan apply

  $ ip a
  ```

  50-cloud-init.yaml

  ```yaml
  network:
      ethernets:
          enp0s3:
              dhcp4: false
              addresses: [192.168.1.202/24]
              gateway4: 192.168.1.1
              nameservers:
                addresses: [8.8.8.8,8.8.4.4,192.168.1.1]
      version: 2
  ```


jetson@nano-4gb-jp461

run_train.sh
  16:13 - 16:57　　　　 == 44分
  17:17 30秒 x 62 epoc == 15分

donkey ui mac 16:49

```
  rsync -r jetson@192.168.100.102:~/mycar/data/ ./data/

  Open Terminal.app // train failed with VS Code Integareted terminal

  cd ./data
  donkey tubclean ./

  python manage.py train --tub ./data/tub_15_19-08-02 --model ./models/mypilot.h5

hugo

  ```
  brew upgrade hugo

  hugo new site doc
  cd doc
  hugo mod init  github.com/McShelby/hugo-theme-relearn
  ```

  https://www.sumsar.net/blog/plain-markdown-blogging-in-hugo/

  https://gohugo.io/content-management/diagrams/#mermaid-diagrams

  https://mcshelby.github.io/hugo-theme-relearn/

jupyter

  https://jupyterbook.org/en/stable/file-types/myst-notebooks.html#convert-a-markdown-file-into-jupytext-myst-markdown

  https://techblog.insightedge.jp/entry/nb-converter

  https://stackoverflow.com/questions/75775058/how-to-open-md-file-like-a-regular-ipynb-inside-jupyter