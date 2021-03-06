import time
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

data = pd.read_csv("Soil_Moisture.csv")
        
data.plot(kind='line',x='Time',y='Moisture',color='green')
#plt.title('Soil Moisture')
plt.ylabel('Soil Moisture (%)')
plt.xlabel(' ')
plt.xticks(rotation = '45')
#plt.show(block=False)
#plt.ion()
plt.show()
        
