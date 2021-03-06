# works with python 2.7.3 and rpi Rasbian 3.18.11v7 and Wireless IMU (android)

import socket, traceback
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

SDD_CONNECTED = True

if SDD_CONNECTED:
    from sdd import disp_num
    a = 13
    b = 5
    c = 12
    d = 16
    e = 21
    f = 19
    g = 26
    pin = [a,b,c,d,e,f,g]

    for p in pin:
        GPIO.setup(p,GPIO.OUT)

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

calibration_counter = 0

try:
    import StringIO
    import csv
    import math

    while 1:

        message, address = s.recvfrom(8192)
        m = csv.reader(StringIO.StringIO(message))
        m = list(m)[0]

        if calibration_counter == 0:
            print "calibrating! Do not move device!"

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
            fil_angle = 0.98*(fil_angle + math.degrees(gx_raw)*dt) + 0.02*a_angle

        if fil_angle > 90:
            dc = 100
        elif fil_angle < 0:
            dc = 0
        else:
            dc = fil_angle

        p.ChangeDutyCycle(dc)

        if SDD_CONNECTED:
            disp_num(int(round(dc/10)), pin)

        # if not calibration_counter % 10:
        print t, g_angle, a_angle, fil_angle, dc%10

        calibration_counter += 1

except (KeyboardInterrupt, SystemExit):
        p.stop()
        GPIO.output(Motor1E, GPIO.LOW)
        GPIO.cleanup()
        raise
except:
        traceback.print_exc()
