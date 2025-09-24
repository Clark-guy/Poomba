import serial
import time

ser = serial.Serial(
        port="/dev/ttyUSB0",
        baudrate=115200,
        timeout=1
)

ser.write(bytes([128]))
time.sleep(0.1)

ser.write(bytes([131]))
time.sleep(0.1)

song = [
        140, 0, 11,
        60, 32,
        69, 32,
        67, 32,
        64, 16,
        60, 16,
        62, 16,
        64, 16,
        62, 16,
        60, 16,
        57, 32,
        55, 32]

ser.write(bytes(song))
time.sleep(0.1)

ser.write(bytes([141,0]))

print('running song')
time.sleep(5)
ser.close()
