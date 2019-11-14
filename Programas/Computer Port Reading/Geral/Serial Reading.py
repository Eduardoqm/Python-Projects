import serial

port = "COM4"
ser = serial.Serial(port, 9600, timeout=4.0)
while True:
    ser.flushInput()
    response = ser.readline().strip()
    values = response.decode('utf-8').split(',')
    print('Soil Moisture = ', values ,'%')
    print(' ')
