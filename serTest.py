import serial,time
ser= serial.Serial('/dev/serial0',115200,timeout=1)
for _ in range (50):
    ser.write(b'\x55')
    ser.flush()
    time.sleep(0.05)
ser.close()
