# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# import psycopg2

# conn = psycopg2.connect(user="postgres",
#                         password="musikklass96",
#                         host="localhost",
#                         port="5432",
#                         database="weather")
# cur = conn.cursor()
# cur.execute("SELECT temperature_2m, relativehumidity_2m, precipitation, time FROM weather_umea")

# results = cur.fetchall()


# #Convert time from VARCHAR to datetime format
# def make_graph():
#     temperature_2m = [result[0] for result in results]
#     relativehumidity_2m = [result[1] for result in results]
#     precipitation = [result[2] for result in results]
#     time = [result[3] for result in results]

#     time = pd.to_datetime(time)
    
#     fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
    
#     ax1.plot(time, temperature_2m, 'b-')
#     ax1.set_xlabel('time')
#     ax1.set_ylabel('temperature_2m', color='b')
#     ax1.tick_params('y', colors='b')
#     ax1.xaxis.set_major_locator(mdates.HourLocator(byhour=range(0,24,24)))
#     ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
#     ax1.grid(True, axis='y', alpha=0.7)
#     ax1_right = ax1.twinx()
#     ax1_right.plot(time, relativehumidity_2m, 'c-')
#     ax1_right.set_ylabel('relativehumidity_2m', color='c')
#     ax1_right.tick_params('y', colors='c')
    
#     ax2.plot(time, precipitation, 'k-')
#     ax2.set_xlabel('time')
#     ax2.set_ylabel('precipitation', color='k')
#     ax2.tick_params('y', colors='k')
#     ax2.xaxis.set_major_locator(mdates.HourLocator(byhour=range(0,24,24)))
#     ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
#     ax2.grid(True, axis='y', alpha=0.7)

#     plt.title('Umeå - Temperature, Humidity and Precipitation')
#     plt.show()
#     plt.savefig("C:\\code\\ETL-riktiga\\harmonized_to_cleanse\\test.png")
#     #plt.savefig("path/to/save/file.png")

# cur.close()
# conn.close()

# make_graph()

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import psycopg2

conn = psycopg2.connect(user="postgres",
                        password="musikklass96",
                        host="localhost",
                        port="5432",
                        database="weather")
cur = conn.cursor()
tables = ['weather_umea', 'weather_trosa', 'weather_varmdo', 'weather_sodertalje']


def plot_weather(table):
    for table in tables:
        cur.execute("SELECT temperature_2m, relativehumidity_2m, precipitation, time FROM {}".format(table))
        results = cur.fetchall()
        temperature_2m = [result[0] for result in results]
        relativehumidity_2m = [result[1] for result in results]
        precipitation = [result[2] for result in results]
        time = [result[3] for result in results]
        time = pd.to_datetime(time)
        fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
        ax1.plot(time, temperature_2m, 'b-')
        ax1.set_xlabel('time')
        ax1.set_ylabel('temperature_2m', color='b')
        ax1.tick_params('y', colors='b')
        ax1.xaxis.set_major_locator(mdates.HourLocator(byhour=range(0,24,24)))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
        ax1.grid(True, axis='y', alpha=0.7)
        ax1_right = ax1.twinx()
        ax1_right.plot(time, relativehumidity_2m, 'c-')
        ax1_right.set_ylabel('relativehumidity_2m', color='c')
        ax1_right.tick_params('y', colors='c')
        ax2.plot(time, precipitation, 'k-')
        ax2.set_xlabel('time')
        ax2.set_ylabel('precipitation', color='k')
        ax2.tick_params('y', colors='k')
        ax2.xaxis.set_major_locator(mdates.HourLocator(byhour=range(0,24,24)))
        ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
        ax2.grid(True, axis='y', alpha=0.7)
        plt.title('{} - Temperature, Humidity and Precipitation'.format(table))
        plt.savefig("harmonized_to_cleansed/{}file.png".format(table))
        cur.close()
        conn.close()


if __name__ == '__main__':
    plot_weather()