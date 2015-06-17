import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)
 
Motor1A = 24
pwm_pin = 23
Motor1E = 25
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(pwm_pin, GPIO.OUT)
p = GPIO.PWM(pwm_pin, 1000)
GPIO.setup(Motor1E,GPIO.OUT)
try:
	GPIO.output(Motor1E, GPIO.HIGH)
	GPIO.output(Motor1A, GPIO.LOW)
	p.start(0)
	while 1:
		for i in range(1,101,5):
			p.ChangeDutyCycle(i)
			sleep(0.5)
		for i in range(1,101,5):
			p.ChangeDutyCycle(101-i)
			sleep(0.5)
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
