import socket, traceback
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

GPIO.output(Motor1E, GPIO.HIGH)
GPIO.output(Motor1A, GPIO.LOW)
p.start(0)

host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))
while 1:
	try:
		message, address = s.recvfrom(8192)
		print message
	except (KeyboardInterrupt, SystemExit):
		p.stop()
		GPIO.output(Motor1E, GPIO.LOW)
		GPIO.cleanup() 
		raise
	except:
		traceback.print_exc()
