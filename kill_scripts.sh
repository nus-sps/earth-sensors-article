#!/usr/bin/sh
if pgrep -f "python3 measurements.py" > /dev/null ; then
	echo "A running measurements.py process has been detected. Terminating ..."
	pkill -f -SIGTERM "python3 measurements.py"
	sleep 2
	if ! pgrep -f "python3 measurements.py" > /dev/null ; then
		echo "measurements.py terminated successfully"
	else
		echo "Failed to terminate measurements.py"
	fi
else
	echo "No running measurements.py process has been detected."
fi

