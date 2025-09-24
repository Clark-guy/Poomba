import serial
import time

ser = serial.Serial(
        port="/dev/serial0",
        baudrate=115200,
        timeout=1
)

ser.write(bytes([128]))
time.sleep(0.1)

ser.write(bytes([131]))
time.sleep(0.1)

ser.write(bytes([142, 25]))
response = ser.read(2)
print('battery: ', response)
