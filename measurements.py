from sensor import *
import time

""" 
sensor.py has the following functions: 
1) connectPiToSensor() -> This function will connect the sensor to the Pi and ensures the connection between the Raspberry Pi and sensor is working 

2) getReading(sensor) -> This function will parse the input from the carbon dioxide sensor and output a carbon dioxide concentration value (in ppm). The input to this function is the output of the connectPiToSensor() functional call. 

Please you these functions to write your own code. 
"""

# Your code goes here! 

sensor = connectPiToSensor()

while True:
	f = open("CO2.txt","a+")
	reading = getReading(sensor)
	f.write("Current date & time " + time.strftime("%c") + str(reading) + " \n")
	time.sleep(10)
	f.close()