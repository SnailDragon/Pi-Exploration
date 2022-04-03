import RPi.GPIO as gp
from time import sleep
import sys

gp.setmode(gp.BCM)

clk = 18
dout = 21
cs = 16

for pinNum in [clk, dout, cs] : gp.setup(pinNum, gp.OUT)

clkSat = False
doutState = False

try:
	while(True):
		clkSat = False
		gp.output(clk, clkSat)			
		doutState = not doutState	
		gp.output(dout, doutState)
		gp.output(cs, 1)
		print("DONE")
		clkSat = True
		sleep(1)

except KeyboardInterrupt:
	print("--Interrupt--")
	gp.cleanup()
