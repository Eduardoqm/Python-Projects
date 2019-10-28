import serial
#from tkinter import *
#import tkinter.messagebox

port = "COM4"
ser = serial.Serial(port,9600)
value = 0


while 1:
    print(ser.read())
    print(' ')
    if value == "1":
        exit()
    else:
        continue
