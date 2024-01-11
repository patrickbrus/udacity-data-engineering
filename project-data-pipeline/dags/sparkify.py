from datetime import datetime, timedelta
import pendulum
import os
from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator
from airflow.providers.amazon.aws.transfers.s3_to_redshift import S3ToRedshiftOperator
from operators.create_tables import CreateRedshiftTablesOperator
from operators.load_dimensions import LoadDimensionOperator
from operators.data_quality import DataQualityOperator
from operators.load_fact import LoadFactOperator
from helpers.sql_queries import SqlQueries

default_args = {
    'owner': 'udacity',
    'start_date': pendulum.now(),
    'depends_on_past': False,
    #'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'catchup': False
}

@dag(
    default_args=default_args,
    description='Load and transform data in Redshift with Airflow',
    schedule_interval='0 * * * *'
)
def final_project():

    start_operator = EmptyOperator(task_id='Begin_execution')
    
    create_redshift_tables = CreateRedshiftTablesOperator(
        task_id="Create_redshift_tables",
    )

    stage_events_to_redshift = S3ToRedshiftOperator(
        task_id="Stage_events",
        schema="public",
        table="staging_events",
        redshift_conn_id="redshift",
        aws_conn_id="aws_credentials",
        s3_bucket="patrick-data-pipeline-bucket",
        s3_key="log-data",
        copy_options= ["FORMAT AS JSON 's3://patrick-data-pipeline-bucket/log_json_path.json'"]
    )

    stage_songs_to_redshift = S3ToRedshiftOperator(
        task_id='Stage_songs',
        schema="public",
        table="staging_songs",
        redshift_conn_id="redshift",
        aws_conn_id="aws_credentials",
        s3_bucket="patrick-data-pipeline-bucket",
        s3_key="song-data",
        copy_options= ["FORMAT AS JSON 'auto'"]
    )

    load_songplays_table = LoadFactOperator(
        task_id='Load_songplays_fact_table',
        sql_query=SqlQueries.songplay_table_insert
    )

    load_user_dimension_table = LoadDimensionOperator(
        task_id='Load_user_dim_table',
    )

    load_song_dimension_table = LoadDimensionOperator(
        task_id='Load_song_dim_table',
    )

    load_artist_dimension_table = LoadDimensionOperator(
        task_id='Load_artist_dim_table',
    )

    load_time_dimension_table = LoadDimensionOperator(
        task_id='Load_time_dim_table',
    )

    run_quality_checks = DataQualityOperator(
        task_id='Run_data_quality_checks',
    )

    # define task order
    start_operator >> create_redshift_tables
    create_redshift_tables >> [stage_events_to_redshift, stage_songs_to_redshift]
    stage_events_to_redshift >> load_songplays_table
    stage_songs_to_redshift >> load_songplays_table
    load_songplays_table >> [load_user_dimension_table, load_song_dimension_table, load_artist_dimension_table, load_time_dimension_table] >> run_quality_checks

final_project_dag = final_project()