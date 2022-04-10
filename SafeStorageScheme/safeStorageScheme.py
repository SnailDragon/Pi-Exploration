"""
Collects data and writes to a csv, 
writes after a determined cycle count to avoid slowdown from writing too often
"""
#import RPi.GPIO as gp
import time
from random import random

#gp.setmode(BCM)

ID = time.strftime("%H%M%S", time.localtime()) + str(int(random() * 100))
print(ID)
STORING_GAP = 100 # how many cycles to wait until you take the time to save
START_TIME = time.time()
it = 0
data = []
timeStamps = []

try:
    #main loop
    while True:
        #collecting data
        data.append(random())
        timeStamps.append(time.time())

        #saving data
        it += 1
        if(it % STORING_GAP == 0):
            start = time.time()
            with open(f"Results{ID}.csv", 'a') as file:
                for i,t in zip(data,timeStamps) : file.write(str(t) + ", " + str(i) + ", \n")
            #clear stored values
            data.clear()
            timeStamps.clear()
            print("Write time: " + str(time.time() - start))
        

        time.sleep(0.013)

#clean up for debugging 
except KeyboardInterrupt:
    print("--Interrupted--")
    #gp.cleanup()
