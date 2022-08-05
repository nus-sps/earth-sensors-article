#!/usr/bin/sh
SCRIPT_NAME="SP3275_measurements.py"
nohup python3 "$SCRIPT_NAME" > ~/log.txt 2> ~/errors.txt < /dev/null & 
exit
