#!/usr/bin/sh
sudo apt update && sudo apt upgrade
sudo apt autoremove
sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_serial 1
sudo raspi-config nonint do_spi 0
sudo raspi-config nonint do_ssh 0
sudo pip3 install -r requirements.txt
cat crontab.txt | crontab -
echo "Done"
