import os
import pandas as pd
import json
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import psycopg2

# with open('raw_to_harmonized\\2023-01-19_09-47-38_Umea.json') as json_file:
#     data = json.load(json_file)

# hourly = data['hourly']

# df = pd.DataFrame(hourly)

# plt.figure()
# df.plot(x='time', y='temperature_2m', kind='line')

# plt.xlabel('Time')
# plt.ylabel('Temperature (°C)')
# plt.show()


# # data = pd.read_json("raw_to_harmonized\\2023-01-19_09-47-38_Umea.json")

# plt.figure()
# data.plot(x='time', y='temperature_2m', kind='line')
# plt.xlabel('Time')
# plt.ylabel('Temperature (°C)')
# plt.show()

#THIS IS THE ONE

conn = psycopg2.connect(user="postgres",
                        password="musikklass96",
                        host="localhost",
                        port="5432",
                        database="weather")
cur = conn.cursor()
cur.execute("SELECT temperature_2m, relativehumidity_2m, precipitation, time FROM weather_umea")

results = cur.fetchall()

temperature_2m = [result[0] for result in results]
relativehumidity_2m = [result[1] for result in results]
precipitation = [result[2] for result in results]
time = [result[3] for result in results]

#Convert time from VARCHAR to datetime format
time = pd.to_datetime(time)

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

ax1.plot(time, temperature_2m, 'b-')
ax1.set_xlabel('time')
ax1.set_ylabel('temperature', color='b')
ax1.tick_params('y', colors='b')
ax1.xaxis.set_major_locator(mdates.HourLocator(byhour=range(0,24,24)))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
ax1.grid(True, axis='y', alpha=0.7)

ax1.twinx().plot(time, relativehumidity_2m, 'r-')
ax1.set_ylabel('humidity', color='r')
ax1.tick_params('y', colors='r')

ax2.plot(time, precipitation, 'y-')
ax2.set_xlabel('time')
ax2.set_ylabel('precipitation', color='y')
ax2.tick_params('y', colors='y')
ax2.xaxis.set_major_locator(mdates.HourLocator(byhour=range(0,24,24)))
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
ax2.grid(True, axis='y', alpha=0.7)

plt.title('Temperature, Humidity and Precipitation')
plt.show()

cur.close()
conn.close()