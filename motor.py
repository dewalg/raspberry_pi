import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)
 
Motor1A = 23
pwm_pin = 24
Motor1E = 25
 
GPIO.setup(Motor1A,GPIO.OUT)
p = GPIO.PWM(pwm_pin, 50)
GPIO.setup(Motor1E,GPIO.OUT)
try:
	GPIO.output(Motor1E, GPIO.HIGH)
	GPIO.output(Motor1A, GPIO.LOW)
	p.start(0)
	while 1:
		for i in range(1,101):
			p.ChangeDutyCycle(i)
		for i in range(1,101):
			p.ChangeDutyCyle(101-i)
			
	# while 1:
	# 	print "Turning motor on"
	# 	GPIO.output(Motor1A,GPIO.HIGH)
	# 	GPIO.output(Motor1B,GPIO.LOW)
	# 	GPIO.output(Motor1E,GPIO.HIGH)
	# 	sleep(20)
except KeyboardInterrupt:
	p.stop()
	GPIO.output(Motor1E, GPIO.LOW)
	GPIO.cleanup() 
