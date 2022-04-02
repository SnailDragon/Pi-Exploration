"""
Uses a tilt switch turn on/off an LED 
- needs sleep when debugging so that terminal output doesn't get left behind
"""
import RPi.GPIO as GPIO
from time import sleep
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	while True:
		if(GPIO.input(15) == 1):
			GPIO.output(14, GPIO.HIGH)
		else:
			GPIO.output(14, GPIO.LOW)
#		print(GPIO.input(15))
#		sleep(0.1)


except KeyboardInterrupt:
	print("--interupt--")
	GPIO.cleanup()
	
