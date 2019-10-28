import serial

port = "COM4"
ser = serial.Serial(port, 9600, timeout=5.0)
while True:
    ser.flushInput()
    response = ser.readline()
    print(response)
