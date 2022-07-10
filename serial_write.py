import time
import serial

ser = serial.Serial(
        port='/dev/ttyUSB0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)
counter=0

while 1:
        #ser.write(str(counter).encode())
        #ser.write(b'salam')
        #ser.write(int(counter))
        #send = bytes(str(counter), 'utf8')

        cmd = input("Enter to send:") + '\r\n'
        if len(cmd)>0:
            ser.write(cmd.encode())
        else:
            continue

#        string = input("Enter to send: ")
        #string = str(counter) + '\n'
#        send = string.encode('utf8')
#        ser.write(send)

 #       time.sleep(1)
 #       counter += 1


