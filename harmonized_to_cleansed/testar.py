# import pandas as pd
# from sqlalchemy import create_engine'

import sqlalchemy
print(sqlalchemy.__version__)



# #create connection
# engine = create_engine('postgresql://postgres:musikklass96@localhost:5432/weather')

# #write dataframe to a table with preferred name
# def sodertalje():
#     sodertalje = pd.read_json('raw_to_harmonized\\2023-01-19_09-47-38_Sodertalje.json')
#     sodertalje.to_sql('sodertalje', engine, if_exists='append')

# def umea():
#     umea = pd.read_json('raw_to_harmonized\\2023-01-19_09-47-38_Sodertalje.json')
#     umea.to_sql('umea', engine, if_exists='append')

# def trosa():
#     trosa = pd.read_json('raw_to_harmonized\\2023-01-19_09-47-38_Sodertalje.json')
#     trosa.to_sql('trosa', engine, if_exists='append')

# def varmdo():
#     varmdo = pd.read_json('raw_to_harmonized\\2023-01-19_09-47-38_Sodertalje.json')
#     varmdo.to_sql('varmdo', engine, if_exists='append')



#postgres


# conn = psycopg2.connect(host='localhost',
#                        database='weather',
#                        user ='postgres',
#                        port= '5432' 
#                        password='')

# cur =conn.cursor()

# cur.execute("INSERT INTO test (time, temperature_2m, relativehumidity_2m, precipitation) VALUES
#             )

# conn.commit()

# cur.close()

# conn.close(