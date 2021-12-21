import serial
import time
from datetime import datetime

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.1)
utc= datetime.utcnow()

while (True):
    line = ser.readline()
    # hexstr = bytes.fromhex(line)
    utc= datetime.utcnow()
    if (line is not ""):
        print("line", line)#.decode('ascii', 'replace'))
        print("utc", utc)
    time.sleep(0.2)
#.decode('unicode_escape')
