import serial
import time

mySerial = serial.Serial('/dev/serial0', 115200)
time.sleep(2)

while True:
    # mySerial.write(b'Hi\n')  # <---- Send the string ---->
    number = 123.7789
    mySerial.write((str(number) + '\n').encode())  # <---- Send the number --->
    print("Sent")
    # time.sleep(1)
