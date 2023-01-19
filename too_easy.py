import os
import pandas as pd
import json
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt

with open('raw_to_harmonized\\2023-01-19_09-47-38_Umea.json') as json_file:
    data = json.load(json_file)

hourly = data['hourly']

df = pd.DataFrame(hourly)

plt.figure()
df.plot(x='time', y='temperature_2m', kind='line')

plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.show()


# # data = pd.read_json("raw_to_harmonized\\2023-01-19_09-47-38_Umea.json")

# plt.figure()
# data.plot(x='time', y='temperature_2m', kind='line')
# plt.xlabel('Time')
# plt.ylabel('Temperature (°C)')
# plt.show()



#chart from Select-query example

# conn = psycopg2.connect(blabla)

# cur = conn.cursor()

#obs ej korrekt syntax
# cur.execute("SELECT temperature_2m, time FROM umea")
# results = cur.fetchall()
# temperature = [result[0] for result in results]
# time = [result[1] for result in results]

# plt.plot(time, temperature)
# plt.xlabel('Time')
# plt.ylabel('Temperature')
# plt.title('Temperature over Time')

# plt.show()



#twinx() metod
# conn = psycopg2.connect(blabla)

#obs ej korrekt syntax
#cur.execute("SELECT temperature_2m, time, humidity FROM umea")
# results = cur.fetchall()

# temperature = [result[0] for result in results]
# time = [result[1] for result in results]
# humidity = [result[2] for result in results]

# fig, ax1 = plt.subplots()
# ax1.plot(time, temperature, 'b-')
# ax1.set_xlabel('Time')
# ax1.set_ylabel('Temperature', color='b')
# ax1.tick_params('y', colors='b')

# ax2 = ax1.twinx()
# ax2.plot(time, humidity, 'r-')
# ax2.set_ylabel('Humidity', color='r')
# ax2.tick_params('y', colors='r')

#plt.title('Temperature and Humidity over Time')
#plt.show()

#cur.close()
#conn.close()
