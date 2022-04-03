"""
Code for a single seven segment display digit - 5611AH
Connections:
Segments(A-G): 18, 15, 22, 23, 27, 14, 17
"""

import RPi.GPIO as gp
from time import sleep
import sys

# segments - start at top - go clockwise, then middle
pins = [18,15,22,23,27,14,17]

gp.setmode(gp.BCM)

for i in pins:
	gp.setup(i, gp.OUT)
	gp.output(i, gp.LOW)

try:
	while(True):
		turnOn = str(input("List segments to turn on: "))
		for seg in pins:
			gp.output(seg, gp.LOW)
		#turnOn = [1,1,1,1,1,1,1,1]
		for i in range(len(turnOn)):
			if(turnOn[i] == "1"):	
				gp.output(pins[i%len(pins)], gp.HIGH)	
		sleep(0.1)

except KeyboardInterrupt:
	print("--Interrupted--")
	gp.cleanup()
