import sys
import json
import time
from gpiozero import MotionSensor
from signal import pause

	
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
	print("usage: python motionsensor.py <device pin> <basename>")
