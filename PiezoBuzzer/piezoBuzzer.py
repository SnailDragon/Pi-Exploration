import RPi.GPIO as gp
from time import sleep
import sys

buzPin = 14

gp.setmode(gp.BCM)
gp.setup(buzPin, gp.OUT)

try:
	while(True):
		gp.output(buzPin, gp.HIGH)
		print("BEEP!")
		sleep(0.1)
		gp.output(buzPin, gp.LOW)
		print("NONE")
		sleep(0.5)

except KeyboardInterrupt:
	print("--Interrupted--")
	gp.cleanup()
