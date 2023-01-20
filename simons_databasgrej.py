import json
import os
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:musikklass96@localhost:5432/weather')
folder_name = "raw_to_harmonized"
table_names = ["weather_umea", "weather_sodertalje", "weather_trosa", "weather_varmdo"]

def insert_data_to_dbs(folder_name, table_names):
    # Get the current working directory
    cwd = os.path.abspath(os.path.dirname(__file__))
    # Join the current working directory and the folder name
    folder_path = os.path.join(cwd, folder_name)
    # Loop through the files in the folder
    for filename in os.listdir(folder_path):
        # Extract the location from the file name
        location = filename.split('_')[2].split('.')[0].lower()
        # Open the file
        with open(os.path.join(folder_path, filename)) as json_file:
            data = json.load(json_file)
        # Convert json to dataframe
        df = pd.DataFrame(data)
        # Add location column to dataframe
        df['location'] = location
        # Insert dataframe into sql table
        for table_name in table_names:
            if table_name.endswith(location):
                df.to_sql(table_name, engine, if_exists='replace', index=False)
            else:
                pass

insert_data_to_dbs(folder_name,table_names)