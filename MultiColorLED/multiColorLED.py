"""
Terminal input controls which pins get turned on, setting the colors of the 4-pin multicolor LED
"""
import RPi.GPIO as GPIO
from time import sleep
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT) #blue 
GPIO.setup(19, GPIO.OUT) #green
GPIO.setup(13, GPIO.OUT) #red

try:
	while True:
		red = input("Red: ")
		green = input("Green: ")
		blue = input("Blue: ")
		if(red == "y"):
			print(red)
			GPIO.output(13, GPIO.HIGH)
		else:
			GPIO.output(13, GPIO.LOW)
		if(green == "y"):
			print(green)
			GPIO.output(19, GPIO.HIGH)
		else:
			GPIO.output(19, GPIO.LOW)
		if(blue == "y"):
			print(blue)
			GPIO.output(26, GPIO.HIGH)
		else:
			GPIO.output(26, GPIO.LOW)
		
except KeyboardInterrupt:
	print("--Interrupted--")
	GPIO.cleanup()
