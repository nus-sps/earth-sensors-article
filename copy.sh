#!/usr/bin/sh
while true
do
	df --output=target | grep /media/$USER | xargs -r -n 1 -d '\n' cp "/home/$USER/*.csv"
	sleep 10
done
