import pandas as pd
import matplotlib.pyplot as plt
import json
import os

#fortsätt här, ta vad som helst!
# #chart
plt.figure()
df.plot(x='time', y='temperature_2m', kind='line')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.show()
