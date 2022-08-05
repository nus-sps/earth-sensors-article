#!/usr/bin/sh
OUTPUT_FILE="SP3175 Sensor Readings.csv"
watch -d -t -n 1  "head -v -n 1 ~/\"$OUTPUT_FILE\" ; tail ~/\"$OUTPUT_FILE\""
