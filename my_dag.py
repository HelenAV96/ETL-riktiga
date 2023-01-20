import pandas as pd
from datetime import datetime
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import Variable
from airflow.operators.bash import BashOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta
import sys
sys.path.append('wsl.localhost\Ubuntu\home\helenav\ETL-riktiga')
from simons_databasgrej import insert_data_to_dbs
from etl_meteo import request_new_weather_data, transform, rename
from too_easy import make_graph

args = {
    'owner': 'Helen ALbandak',
    'start_date': datetime(2023, 1, 1), # make start date in the past
    'depends_on_past': False,
    'retries': 1,
    'retry_delay':timedelta(minutes=5)
}

dag = DAG(
    dag_id='my_dag',
    default_args=args,
    schedule='@daily' # make this workflow happen every day
)

with dag:

    request_new_weather_data = PythonOperator(
        task_id='request_new_weather_data',
        python_callable= request_new_weather_data,
        #provide_context=True,
        do_xcom_push=True
    )
    transform = PythonOperator(
        task_id='transform',
        python_callable= transform,
        do_xcom_push=True
        # provide_context=True
    )
    rename= PythonOperator(
        task_id='rename',
        python_callable= rename,
        do_xcom_push=True
        # provide_context=True
    )

    insert_data_to_dbs = PythonOperator(
        task_id='insert_data_to_db',
        python_callable= insert_data_to_dbs,
        do_xcom_push=True
        # provide_context=True
    )

    make_graph = PythonOperator(
        task_id='make_graph',
        python_callable= make_graph,
        #provide_context=True,
        do_xcom_push=True
    )
