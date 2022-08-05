#!/usr/bin/sh
sudo apt update && sudo apt upgrade
sudo apt autoremove
sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_serial 2
sudo raspi-config nonint do_spi 0
sudo raspi-config nonint do_ssh 0
sudo raspi-config nonint do_blanking 1
sudo pip3 install -r requirements.txt
cat crontab.txt | crontab -
ln -s $PWD/live_copy.sh $PWD/start_script.sh $PWD/kill_scripts.sh $PWD/shutdown_pi.sh ~/
ln -s $PWD/live_results.sh ~/
echo "Done"
