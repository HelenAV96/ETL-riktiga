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
    insert_data_to_dbs = PythonOperator(
        task_id='insert_data_to_db',
        python_callable= insert_data_to_dbs,
        # provide_context=True
    )
