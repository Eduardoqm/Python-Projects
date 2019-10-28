import serial
from serial import Serial

ser = serial.Serial(port='COM4', baudrate=9600, bytesize=serial.EIGHTBITS, parity = serial.PARITY_NONE, timeout=2)
try:
	ser.isOpen()
	print('Serial port is open')
except:
	print('Error')
	exit()
	
if(ser.isOpen()):
	try:
		while(i):
			print(ser.read())
	except Exception:
		print('error')
else:
	print('Cannot open serial port')
