import adafruit_bme680
import board
import busio
import serial
import time
from sys import exit

def connect_to_bme688_sensor():
	try:
		i2c = busio.I2C(board.SCL, board.SDA)
		bme688_sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)
	except:
		print("Could not connect to BME688 sensor, retrying")
		try:
			i2c = busio.I2C(board.SCL, board.SDA)
			bme688_sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)
		except:
			print("Still could not connect to BME688 sensor, exiting")
			raise
	return bme688_sensor

def connect_to_CO2_sensor():
	"""
	Helper function to connect Pi to Sensor
	"""
	SERIAL_PORT = "/dev/ttyS0"
	try:
		sensor = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 0.8)
		sensor.reset_input_buffer()
		sensor.reset_output_buffer()
	except:
		print("Could not connect to CO2 sensor, retrying")
		try:
			sensor = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 0.8)
			sensor.reset_input_buffer()
			sensor.reset_output_buffer()
		except:
			print("Still could not connect to CO2 sensor, exiting")
			raise

	time.sleep(1)
	return sensor

def get_CO2_reading(sensor):
	"""
	To parse sensor input for carbon dioxide reading
	"""
	# start_time = time.time()
	sensor.reset_input_buffer()
	# sensor.reset_output_buffer()
	sensor.write(b"\xFE\x44\x00\x08\x02\x9F\x25")
	time.sleep(0.5)
	for i in range(5):
		resp = sensor.read(7)
		if resp != b'':
			break
	if resp == b'':
		raise TimeoutError("No reading after 5 attempts")
	high = resp[3]
	low = resp[4]
	co2 = (high*256) + low
	# print(f"Measurement duration : {time.time() - start_time} s")
	return co2

def close_CO2_sensor(sensor):
	sensor.close()

if __name__ == "__main__":
	co2_sensor = connect_to_CO2_sensor()
	bme_sensor = connect_to_bme688_sensor()
	while True:
		print(f"{get_CO2_reading(co2_sensor) = }, \n{bme_sensor.temperature = }, \n{bme_sensor.relative_humidity = }, \n{bme_sensor.pressure = }, \n{bme_sensor.gas =}")

		time.sleep(5)
	sensor.close()
