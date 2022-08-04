#!/usr/bin/sh
nohup python3 SP3275_measurements.py > ~/log.txt 2> ~/errors.txt < /dev/null & 
exit
