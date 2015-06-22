import socket, traceback

host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))

calibration_counter = 0

while 1:
    try:
        import StringIO
        import csv
        import math

        message, address = s.recvfrom(8192)
        m = csv.reader(StringIO.StringIO(message))
        m = list(m)[0]

        if calibration_counter == 0:
            print "calibrating! Do not move device!"
            t = float(m[0])
            gx = 0
            gx_raw = 0
            offset = 0
            calibration_counter += 1
            continue

        prev_t = float(m[0])
        dt = abs(prev_t - t)
        t = prev_t

        try:
            gx_raw = float(m[6])
        except:
            pass

        if calibration_counter < 11 and calibration_counter > 0:
            gx = gx + math.degrees(gx_raw)*dt
            calibration_counter += 1
            continue

        if calibration_counter == 11:
            offset = gx/10
            print "Done calibrating. Offset value:" + str(offset)
            calibration_counter += 1
            continue

        if calibration_counter > 11:
            gx = gx + math.degrees(gx_raw)*dt - offset

        if not calibration_counter % 10:
            print t, gx

        calibration_counter += 1

    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
