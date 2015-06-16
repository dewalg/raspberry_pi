# python 3 using RPi GPIO library
# test commit

import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)

led = 22
wait = 1 # in seconds
gp.setup(led, gp.OUT)

try:
	while 1:
		gp.output(led, gp.LOW)
		time.sleep(wait)
		gp.output(led, gp.HIGH)
		time.sleep(wait)
except KeyboardInterrupt:
	gp.cleanup()
	
