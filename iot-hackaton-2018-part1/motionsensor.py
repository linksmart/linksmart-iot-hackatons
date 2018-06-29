#!/usr/bin/python
#from __future__ import print_function
import sys
import json
import time
from gpiozero import MotionSensor
from signal import pause

#def eprint(*args, **kwargs):
#    print(*args, file=sys.stderr, **kwargs)
	
pin = 4
bn = ""
def motion_detected_cb():
	global  bn;
	now = int(round(time.time()))
	value = {"bn": bn+"Motion", "e":[{"bv": True}]}
	print(json.dumps(value))

if len(sys.argv) == 3:
	pin = int(sys.argv[1])
	bn = sys.argv[2]
	pir = MotionSensor(pin)
	
	pir.when_motion= motion_detected_cb
	print("ready for events")
	pause()
else:
	eprint("usage: python motionsensor.py <device pin> <basename>")