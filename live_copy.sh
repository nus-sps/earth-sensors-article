#!/usr/bin/sh
OUTPUT_FILE="SP3275 Sensor Readings.csv"
watch -d -t -n 1 "df --output=target | grep /media/$USER | xargs -s 100000 -I{} -n 1 -d '\n' tail -v {}/\"$OUTPUT_FILE\""
