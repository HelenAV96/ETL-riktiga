import json
import os

import pandas as pd
from sqlalchemy import create_engine





engine = create_engine('postgresql://postgres:musikklass96@localhost:5432/weather')
folder_name = "raw_to_harmonized"
table_names = ["weather_umea", "weather_sodertalje", "weather_trosa", "weather_varmdo"]

def insert_data_to_dbs(folder_name, table_names):
    # Loop through the files in the folder
    for filename in os.listdir(folder_name):
        # Extract the location from the file name
        location = filename.split('_')[2].split('.')[0].lower()
        # Open the file
        with open(folder_name + '/' + filename) as json_file:
            data = json.load(json_file)
        # Convert json to dataframe
        df = pd.DataFrame(data)
        # Add location column to dataframe
        df['location'] = location
        # Insert dataframe into sql table
        for table_name in table_names:
            if table_name.endswith(location):
                df.to_sql(table_name, engine, if_exists='append', index=False)
            else:
                pass


insert_data_to_dbs(folder_name,table_names)