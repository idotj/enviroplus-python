#!/usr/bin/env python

import time
from bme280 import BME280

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

print("""weather.py - Print readings from the BME280 weather sensor.

Press Ctrl+C to exit!

""")

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

while True:
    temperature = bme280.get_temperature()
    pressure = bme280.get_pressure()
    humidity = bme280.get_humidity()
    print("""Temperature: {:05.2f} *C
Pressure: {:05.2f} hPa
Relative humidity: {:05.2f} %
""".format(temperature, pressure, humidity))
    time.sleep(1)
