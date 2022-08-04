#!/usr/bin/sh
sudo pip3 install -r requirements.txt
cat crontab.txt | crontab -
echo "Done"
