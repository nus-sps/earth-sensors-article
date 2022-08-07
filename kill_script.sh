#!/usr/bin/sh
SCRIPT_NAME="SP3275_measurements.py"
if pgrep -f "$SCRIPT_NAME" > /dev/null ; then
	echo "A running $SCRIPT_NAME process has been detected. Terminating ..."
	pkill -f -SIGTERM "$SCRIPT_NAME"
	sleep 2
	if ! pgrep -f "$SCRIPT_NAME" > /dev/null ; then
		echo "$SCRIPT_NAME terminated successfully"
	else
		echo "$SCRIPT_NAME still running after 2s, should terminate soon"
	fi
else
	echo "No running $SCRIPT_NAME process has been detected, exiting"
fi

