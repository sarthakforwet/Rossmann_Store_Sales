from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python import PythonVirtualenvOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 11, 15),
    'depends_on_past': False,
    'email': ['khandelwal.sarth@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
}

dag = DAG('fetch_rossman_data',
          default_args=default_args,
          description='Runs an external Python script',
          schedule_interval='@daily',
          catchup=False)

with dag:
    # setup_kaggle = BashOperator(
    #     task_id = 'setup_kaggle_credentials',
    #     bash_command = '''
    #     mkdir -p /home/airflow/.config
    #     mkdir -p /home/airflow/.config/kaggle
    #     cp /home/airflow/gcs/dags/data/kaggle.json /home/airflow/.config/kaggle/
    #     chmod 600 /home/airflow/.config/kaggle/kaggle.json
    #     '''
    # )

    run_script_task = BashOperator(
        task_id='run_script',
        bash_command='python /home/airflow/gcs/dags/scripts/extract_and_push_to_gcs.py',
    )


