#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# The script has been modified to print measurements in SenML format. 
import sys
import json
import Adafruit_DHT
import time

# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 4 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
    bn = sys.argv[3]
else:
    print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpinNo BaseName')
    print('example: sudo ./getSensorValue.py 22 4 hostname_of_device/')
    sys.exit(1)

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
if humidity is not None and temperature is not None:
    now = int(round(time.time()))
    value = {"bn": bn, "e":[{"n":"Temperature", "u": "Cel", "v": temperature, "t": now}, {"n":"Humidity", "u": "%RH", "v": humidity, "t": now}]}
    print(json.dumps(value))
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)