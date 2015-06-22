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

DEBUG_MODE = False

while 1:
	try:
		import StringIO
        import csv
        import math
        import plotly.plotly as py
        from plotly.graph_objs import *

        message, address = s.recvfrom(8192)
        m = csv.reader(StringIO.StringIO(message))
        m = list(m)[0]

        if calibration_counter == 0:
            print "calibrating! Do not move device!"

            ## initiate the real-time plotting
            if DEBUG_MODE:
                trace1 = Scatter(x=[], y=[], stream=dict(token='yx22lx9rw1'))
                trace2 = Scatter(x=[], y=[], stream=dict(token='vpc456qm13'))
                trace3 = Scatter(x=[], y=[], stream=dict(token='k7o9t5gowj'))
                data = Data([trace1, trace2, trace3])
                py.plot(data)
                st1 = py.Stream('yx22lx9rw1')
                st2 = py.Stream('vpc456qm13')
                st3 = py.Stream('k7o9t5gowj')
                st1.open()
                st2.open()
                st3.open()

            t = float(m[0])
            g_angle = 0
            gx_raw = 0
            ax_raw = 0
            ay_raw = 0
            az_raw = 0
            offset = 0
            fil_angle = 0
            calibration_counter += 1
            continue

        prev_t = float(m[0])
        dt = abs(prev_t - t)
        t = prev_t

        try:
            gx_raw = float(m[6])
            ax_raw = float(m[2])
            ay_raw = float(m[3])
            az_raw = float(m[4])
        except:
            pass

        if calibration_counter < 11 and calibration_counter > 0:
            g_angle = g_angle + math.degrees(gx_raw)*dt
            calibration_counter += 1
            continue

        if calibration_counter == 11:
            offset = g_angle/10
            print "Done calibrating. Offset value:" + str(offset)
            calibration_counter += 1
            continue

        if calibration_counter > 11:
            a_angle = math.degrees(math.atan(ay_raw/(pow(ax_raw,2)+pow(az_raw,2))))
            g_angle = g_angle + math.degrees(gx_raw)*dt - offset
            fil_angle = 0.995*(fil_angle + math.degrees(gx_raw)*dt) + 0.005*a_angle

        if DEBUG_MODE and not calibration_counter % 5:
            st1.write(dict(x=t, y=g_angle))
            st2.write(dict(x=t, y=a_angle))
            st3.write(dict(x=t, y=fil_angle))

        if fil_angle > 90:
            dc = 100
        else
            dc = fil_angle

        p.ChangeDutyCycle(dc)

        # if not calibration_counter % 10:
        print t, g_angle, a_angle, fil_angle

        calibration_counter += 1
	except (KeyboardInterrupt, SystemExit):
        if DEBUG_MODE:
            st1.close()
            st2.close()
            st3.close()
		p.stop()
		GPIO.output(Motor1E, GPIO.LOW)
		GPIO.cleanup()
		raise
	except:
		traceback.print_exc()
