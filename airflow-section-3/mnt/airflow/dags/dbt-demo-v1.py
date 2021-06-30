from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import datetime
from airflow.utils.dates import timedelta

default_args = {
    'owner': 'astronomer',
    'depends_on_past': False,
    'start_date': datetime(2020, 12, 23),
    'email': ['noreply@astronomer.io'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}
dag = DAG(
    'dbt_dag_v2',
    default_args=default_args,
    description='An Airflow DAG to invoke simple dbt commands',
    schedule_interval=timedelta(days=1),
)

dbt_run = BashOperator(
    task_id='dbt_run',
    bash_command='dbt run',
    dag=dag
)

dbt_test = BashOperator(
    task_id='dbt_test',
    bash_command='dbt test',
    dag=dag
)

dbt_run >> dbt_test