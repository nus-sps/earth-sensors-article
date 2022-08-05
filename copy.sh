#!/usr/bin/sh
OUTPUT_FILE="SP3175 Sensor Readings.csv"
while true
do
	df --output=target | grep /media/$USER | xargs -r -n 1 -d '\n' cp "/home/$USER/$OUTPUT_FILE"
	sleep 10
done
