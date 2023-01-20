## Create an ETL process to load the data from open-meteo.com into a json file


import requests
import json
import pandas as pd
import numpy as np
import os
import datetime 
import shutil
# Get the data from open-meteo.com



list_of_locations = [{"latitude":"62.8","longitude":"20.26"},
                    {"latitude":"59.19","longitude":"17.62"},
                    {"latitude":"58.89","longitude":"17.55"},
                    {"latitude":"59.33","longitude":"18.59"}]


url = "https://api.open-meteo.com/v1/forecast"

#log each request to a new json named after the date and time annd location

def request_new_weather_data():
    #delete all files in source_to_raw
    for filename in os.listdir('source_to_raw'):
        os.remove('source_to_raw/' + filename)
        
    for location in list_of_locations:
        querystring = {"latitude":location["latitude"],"longitude":location["longitude"],"hourly":["temperature_2m","relativehumidity_2m","precipitation"],"windspeed_unit":"ms","timezone":"auto"}
        response = requests.request("GET", url, params=querystring)
        data = response.json()
        now = datetime.datetime.now()
        filename = "source_to_raw/" + now.strftime("%Y-%m-%d_%H-%M-%S") + "_" + location["latitude"] + "_" + location["longitude"] + ".json"
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)

    print("Data fetched from open-meteo.com and saved to source_to_raw/")


def transform():
    #delete all files in raw_to_harmonized
    for filename in os.listdir('raw_to_harmonized'):
        os.remove('raw_to_harmonized/' + filename)

    for filename in os.listdir('source_to_raw'):
        with open('source_to_raw/' + filename) as json_file:
            data = json.load(json_file)
        hourly = data['hourly']
        df = pd.DataFrame(hourly)
        df.to_json('raw_to_harmonized/' + filename)

    print("Data transformed and saved to raw_to_harmonized/")

def rename():
    for filename in os.listdir('raw_to_harmonized'):
        if filename.endswith("62.8_20.26.json"):
            shutil.move('raw_to_harmonized/' + filename, 'raw_to_harmonized/' + filename.replace("62.8_20.26", "Umea"))
        elif filename.endswith("59.19_17.62.json"):
            shutil.move('raw_to_harmonized/' + filename, 'raw_to_harmonized/' + filename.replace("59.19_17.62", "Sodertalje"))
        elif filename.endswith("58.89_17.55.json"):
            shutil.move('raw_to_harmonized/' + filename, 'raw_to_harmonized/' + filename.replace("58.89_17.55", "Trosa"))
        elif filename.endswith("59.33_18.59.json"):
            shutil.move('raw_to_harmonized/' + filename, 'raw_to_harmonized/' + filename.replace("59.33_18.59", "Varmdo"))
        
    print("Data renamed to match the format YYYY-MM-DD_HH-MM-SS_(PLACE).json")

if __name__ == "__main__":
    request_new_weather_data(),transform(), rename()






            



request_new_weather_data()
transform()
rename()