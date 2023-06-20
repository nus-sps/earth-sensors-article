#!/usr/bin/sh
OUTPUT_FILE="SP3275 Sensor Readings.csv"
while true
do
	df --output=target | grep /media/pi | xargs -r -n 1 -d '\n' cp "/home/pi/$OUTPUT_FILE"
	sleep 10
done
