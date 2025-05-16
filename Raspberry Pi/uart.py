import serial
import time

ser = serial.Serial('/dev/serial0', 115200)
time.sleep(2)

while True:
    # ser.write(b'Hi\n')  # Send the string
    number = 123.7789
    ser.write((str(number) + '\n').encode())  # Send the number
    print("Sent")
    # time.sleep(1)
