cmdline

```
console=serial0,115200 console=tty1 root=PARTUUID=35684e8a-02 rootfstype=ext4 fsck.repair=yes rootwait modules-load=dwc2,g_ether quiet splash plymouth.ignore-serial-consoles cfg80211.ieee80211_regdom=JP cfg80211.ieee80211_regdom=JP systemd.run=/boot/firstrun.sh systemd.run_success_action=reboot systemd.unit=kernel-command-line.target
```

----

config

```
# For more options and information see
# http://rptl.io/configtxt
# Some settings may impact device functionality. See link above for details

# Uncomment some or all of these to enable the optional hardware interfaces
#dtparam=i2c_arm=on
#dtparam=i2s=on
#dtparam=spi=on

# Enable audio (loads snd_bcm2835)
dtparam=audio=on

# Additional overlays and parameters are documented
# /boot/firmware/overlays/README

# Automatically load overlays for detected cameras
camera_auto_detect=1

# Automatically load overlays for detected DSI displays
display_auto_detect=1

# Automatically load initramfs files, if found
auto_initramfs=1

# Enable DRM VC4 V3D driver
dtoverlay=vc4-kms-v3d
max_framebuffers=2

# Don't have the firmware create an initial video= setting in cmdline.txt.
# Use the kernel's default instead.
disable_fw_kms_setup=1

# Run in 64-bit mode
arm_64bit=1

# Disable compensation for displays with overscan
disable_overscan=1

# Run as fast as firmware / board allows
arm_boost=1

[cm4]
# Enable host mode on the 2711 built-in XHCI USB controller.
# This line should be removed if the legacy DWC2 controller is required
# (e.g. for USB device mode) or if USB support is not required.
otg_mode=1

[all]
dtoverlay=dwc2
#dtoverlay=dwc2,dr_mode=peripheral
#dtoverlay=disable-wifi
```

----

fistrun

```
#!/bin/bash

set +e

CURRENT_HOSTNAME=`cat /etc/hostname | tr -d " \t\n\r"`
if [ -f /usr/lib/raspberrypi-sys-mods/imager_custom ]; then
   /usr/lib/raspberrypi-sys-mods/imager_custom set_hostname donkey-yolo
else
   echo donkey-yolo >/etc/hostname
   sed -i "s/127.0.1.1.*$CURRENT_HOSTNAME/127.0.1.1\tdonkey-yolo/g" /etc/hosts
fi
FIRSTUSER=`getent passwd 1000 | cut -d: -f1`
FIRSTUSERHOME=`getent passwd 1000 | cut -d: -f6`
if [ -f /usr/lib/raspberrypi-sys-mods/imager_custom ]; then
   /usr/lib/raspberrypi-sys-mods/imager_custom enable_ssh
else
   systemctl enable ssh
fi
if [ -f /usr/lib/userconf-pi/userconf ]; then
   /usr/lib/userconf-pi/userconf 'pi' '$5$3BPKOg/ro5$qModyv.11HQmIyRVf4BZ7PIn0dFe2yxq0l2v5z5BoV1'
else
   echo "$FIRSTUSER:"'$5$3BPKOg/ro5$qModyv.11HQmIyRVf4BZ7PIn0dFe2yxq0l2v5z5BoV1' | chpasswd -e
   if [ "$FIRSTUSER" != "pi" ]; then
      usermod -l "pi" "$FIRSTUSER"
      usermod -m -d "/home/pi" "pi"
      groupmod -n "pi" "$FIRSTUSER"
      if grep -q "^autologin-user=" /etc/lightdm/lightdm.conf ; then
         sed /etc/lightdm/lightdm.conf -i -e "s/^autologin-user=.*/autologin-user=pi/"
      fi
      if [ -f /etc/systemd/system/getty@tty1.service.d/autologin.conf ]; then
         sed /etc/systemd/system/getty@tty1.service.d/autologin.conf -i -e "s/$FIRSTUSER/pi/"
      fi
      if [ -f /etc/sudoers.d/010_pi-nopasswd ]; then
         sed -i "s/^$FIRSTUSER /pi /" /etc/sudoers.d/010_pi-nopasswd
      fi
   fi
fi
if [ -f /usr/lib/raspberrypi-sys-mods/imager_custom ]; then
   /usr/lib/raspberrypi-sys-mods/imager_custom set_wlan 'Galaxy A23 kwiksher' '3ed28710b41086b4940c3938c56552f7a4db5517fe5110627452a3f05c78f986' 'JP'
else
cat >/etc/wpa_supplicant/wpa_supplicant.conf <<'WPAEOF'
country=JP
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
ap_scan=1

update_config=1
network={
	ssid="Galaxy A23 kwiksher"
	psk=xxxxxx
}

WPAEOF
   chmod 600 /etc/wpa_supplicant/wpa_supplicant.conf
   rfkill unblock wifi
   for filename in /var/lib/systemd/rfkill/*:wlan ; do
       echo 0 > $filename
   done
fi
if [ -f /usr/lib/raspberrypi-sys-mods/imager_custom ]; then
   /usr/lib/raspberrypi-sys-mods/imager_custom set_keymap 'jp'
   /usr/lib/raspberrypi-sys-mods/imager_custom set_timezone 'Asia/Tokyo'
else
   rm -f /etc/localtime
   echo "Asia/Tokyo" >/etc/timezone
   dpkg-reconfigure -f noninteractive tzdata
cat >/etc/default/keyboard <<'KBEOF'
XKBMODEL="pc105"
XKBLAYOUT="jp"
XKBVARIANT=""
XKBOPTIONS=""

KBEOF
   dpkg-reconfigure -f noninteractive keyboard-configuration
fi

cat << EOF > /etc/network/interfaces.d/usb0
auto usb0
allow-hotplug usb0
iface usb0 inet static
    address 192.168.2.2
    netmask 255.255.255.0
    gateway 192.168.2.1
EOF

rm -f /boot/firstrun.sh
sed -i 's| systemd.run.*||g' /boot/cmdline.txt
exit 0
````