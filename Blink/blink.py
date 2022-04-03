"""
Blinks LED  on pin 14 
"""

import RPi.GPIO as gp
from time import sleep

gp.setmode(gp.BCM)

gp.setup(14, gp.OUT)

while True:
	gp.output(14, gp.LOW)

	sleep(1)

	gp.output(14, gp.HIGH)

	sleep(1)

gp.cleanup() 

