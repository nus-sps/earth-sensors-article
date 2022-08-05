#!/usr/bin/python3
import csv
import time
import signal
from os import listdir
from os import path
from sensors import connect_to_CO2_sensor, get_CO2_reading, connect_to_bme688_sensor
from sys import exit
from threading import Thread

def sleep_till(target_time):
	duration = target_time - time.time()
	if duration < 0:
		return
	if duration > 0.1:
		time.sleep(duration - 0.1)
	while target_time - time.time() > 0.01:
		time.sleep(0.01)

def signal_handler(sig_num, stack_frame):
	print("Received signal, stopping")
	csvfile.flush()
	csvfile.close()
	exit()

MEASUREMENT_INTERVAL = 5
OUTPUT_FILE = path.expanduser("~/SP3275 Sensor Readings.csv")

if not path.exists(OUTPUT_FILE):
	with open(OUTPUT_FILE, mode = "a", buffering = 1) as csvfile:
		csv_writer = csv.writer(csvfile)
		csv_writer.writerow(("CO2", "Temperature", "Humidity", "Pressure", "Gas"))

with open(OUTPUT_FILE, mode = "a", buffering = 1) as csvfile:
	csv_writer = csv.writer(csvfile)

	CO2_sensor = connect_to_CO2_sensor()
	bme688_sensor = connect_to_bme688_sensor()

	signal.signal(signal.SIGINT, signal_handler)
	signal.signal(signal.SIGTERM, signal_handler)

	start_time = time.time()
	while True:
		# loop_start_time = time.time()
		timer_thread = Thread(target = sleep_till, args = (start_time + MEASUREMENT_INTERVAL,))
		timer_thread.start()
		start_time += MEASUREMENT_INTERVAL
		CO2 = get_CO2_reading(CO2_sensor)
		temp = bme688_sensor.temperature
		hum = bme688_sensor.relative_humidity
		pressure = bme688_sensor.pressure
		gas = bme688_sensor.gas
		# print(f"CO2: {CO2}, T: {temp}, H: {hum}, P: {pressure}, G: {gas}")
		# print(f"Measurement duration : {time.time() - loop_start_time} s")
		csv_writer.writerow((CO2, temp, hum, pressure, gas))
		csvfile.flush()

		timer_thread.join()

