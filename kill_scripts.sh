#!/usr/bin/sh
if (pgrep -a python3 measurements.py | wc -l)
	pkill python3
	echo "Measurements.py terminated"
	else
		echo "Measurements.py is already not running"

