# python 3 using RPi GPIO library
import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)

led = 22
wait = 0.05 # in seconds
gp.setup(led, gp.OUT)

try:
	while 1:
		gp.output(led, gp.LOW)
		time.sleep(wait)
		gp.output(led, gp.HIGH)
		time.sleep(wait)
except KeyboardInterrupt:
	gp.cleanup()
	
