import serial
import time
import csv
import pandas as pd

global df
port = "COM4"
ser = serial.Serial(port, 9600, timeout=3.0)
ser.flushInput()
df = pd.DataFrame({'Time':[float(0)], 'Moisture':[float(0)]})


while True:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
        #with open("test_data.csv","a") as f:
            #writer = csv.writer(f,delimiter=",")
            #writer.writerow([time.time(),decoded_bytes])

        df_input = pd.DataFrame({'Time':[float(time.time())], 'Moisture':[float(decoded_bytes)]})
        df_add = [df, df_input]
        df_master = pd.concat(df_add, ignore_index=True)
        df = df_master
        df.to_csv('Test_COM4.csv')

    except:
        print("Keyboard Interrupt")
        break
