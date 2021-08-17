import serial 
import time 

def connectPiToSensor():
	""" 
	Helper function to connect Pi to Sensor 
	"""
	ser = serial.Serial("/dev/serial0", baudrate = 9600, timeout = 0.5)
	ser.flushInput()
	time.sleep(1)
	return ser 

def getReading(ser):
	""" 
	To parse sensor input for carbon dioxide reading 
	"""
	ser.flushInput()
    ser.write("\xFE\x44\x00\x08\x02\x9F\x25")
    time.sleep(0.5)
    resp = ser.read(7)
    high = ord(resp[3])
    low = ord(resp[4])
    co2 = (high*256) + low
    return co2