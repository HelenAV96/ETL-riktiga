from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
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
