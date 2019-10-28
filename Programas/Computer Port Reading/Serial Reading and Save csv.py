import serial
import time
import csv

port = "COM4"
ser = serial.Serial(port, 9600, timeout=5.0)
while True:
    ser.flushInput()
    response = ser.readline()
    print(response)
    with open("Test_COM4.csv","a") as f:
        writer = csv.writer(f,delimiter=",")
        writer.writerow([time.time(),response])
