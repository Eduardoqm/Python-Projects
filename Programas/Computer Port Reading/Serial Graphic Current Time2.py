import serial
import time
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates



while True:
    try:
        global df
        data = pd.read_csv("Test_COM4.csv")
        plt.close()

        df.plot(kind='line',x='Time',y='Moisture',color='red')
        plt.show(block=False)
        #plt.ion()
        #plt.show() 

    except:
        print("Keyboard Interrupt")
        break
