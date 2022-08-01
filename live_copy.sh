OUTPUT_FILE="SP3175 Sensor Readings.csv"
watch -d -t -n 1 "df --output=target | grep /media/pi | xargs -s 100000 -I{} -n 1 -d '\n' tail -v {}/\"$OUTPUT_FILE\""
