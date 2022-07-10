import serial
import time
from threading import Lock

mutex = Lock() 

sendSerial = serial.Serial ("/dev/ttyUSB0", 9600)
readoutSerial = serial.Serial ("/dev/ttyUSB0", 9600)
time.sleep (2)

mutex.acquire()
try:
    sendSerial.write ("data1" + "data2" + "data3" + "data4")
except:
    pass
finally:
    mutex.release()

while True:
    with mutex:
        readoutSerial.read ("data5" + "data6")
