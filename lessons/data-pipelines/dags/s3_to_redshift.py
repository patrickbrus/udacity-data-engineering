import pendulum
import logging

from airflow.decorators import dag, task
from airflow.secrets.metastore import MetastoreBackend
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.postgres_operator import PostgresOperator


# Use the PostgresHook to create a connection using the Redshift credentials from Airflow 
# Use the PostgresOperator to create the Trips table
# Use the PostgresOperator to run the LOCATION_TRAFFIC_SQL


from udacity.common import sql_statements

@dag(
    start_date=pendulum.now()
)
def load_data_to_redshift():

    @task
    def create_table():
        redshift_hook = PostgresHook(postgres_conn_id="redshift")
        redshift_hook.run(sql_statements.CREATE_TRIPS_TABLE_SQL)

    @task
    def load_task():    
        metastoreBackend = MetastoreBackend()
        aws_connection=metastoreBackend.get_connection("aws_credentials")
        logging.info(vars(aws_connection))
        redshift_hook = PostgresHook("redshift")
        redshift_hook.run(sql_statements.COPY_ALL_TRIPS_SQL.format(aws_connection.login, aws_connection.password))

    @task
    def location_traffic_drop():
        redshift_hook = PostgresHook("redshift")
        redshift_hook.run(sql_statements.LOCATION_TRAFFIC_SQL_DROP)

    @task
    def location_traffic_create():
        redshift_hook = PostgresHook("redshift")
        redshift_hook.run(sql_statements.LOCATION_TRAFFIC_SQL_CREATE)

    # create task dependencies
    create_table_task = create_table()
    load_data_task = load_task()
    location_traffic_drop_task = location_traffic_drop()
    location_traffic_create_task = location_traffic_create()

    create_table_task >> load_data_task >> location_traffic_drop_task >> location_traffic_create_task


s3_to_redshift_dag = load_data_to_redshift()
