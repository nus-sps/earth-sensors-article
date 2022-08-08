# Setup of Raspberry Pi and Carbon Dioxide Sensor. 

Instructions to setting up Raspberry Pi to [K30 10,000 ppm Carbon Dioxide Sensor](https://www.co2meter.com/products/k-30-co2-sensor-module), can be found in `setup-manual.pdf`. Additional python code files used are also provided to parse readings and save them to an output file. 

Instructions for setting up Adafruit BME688 sensor :

[https://learn.adafruit.com/adafruit-bme680-humidity-temperature-barometic-pressure-voc-gas/python-circuitpython](https://learn.adafruit.com/adafruit-bme680-humidity-temperature-barometic-pressure-voc-gas/python-circuitpython)

Command to run in the terminal window after flashing a fresh copy of Raspberry Pi OS:
```
git clone https://github.com/nus-sps/earth-sensors-article && cd earth-sensors-article && ./setup.sh
```
NOTE: The codebase currently depends on the username being set to the default value of "pi".
