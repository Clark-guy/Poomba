import serial
import time

ser = serial.Serial(
        port="/dev/serial0",
        baudrate=115200,
        timeout=1
)

ser.write(b'HELLO\n')
ser.flush()
time.sleep(0.1)

resp = ser.read(20)
print(resp)
ser.close()
