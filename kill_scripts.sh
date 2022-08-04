#!/usr/bin/sh
if pgrep -f "SP3275_measurements.py" > /dev/null ; then
	echo "A running SP3275_measurements.py process has been detected. Terminating ..."
	pkill -f -SIGTERM "SP3275_measurements.py"
	sleep 2
	if ! pgrep -f "SP3275_measurements.py" > /dev/null ; then
		echo "SP3275_measurements.py terminated successfully"
	else
		echo "Failed to terminate SP3275_measurements.py"
	fi
else
	echo "No running SP3275_measurements.py process has been detected."
fi

