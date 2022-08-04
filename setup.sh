#!/usr/bin/sh
sudo apt update && sudo apt upgrade
sudo pip3 install -r requirements.txt
cat crontab.txt | crontab -
echo "Done"
