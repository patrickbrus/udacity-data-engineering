# Sparkify Data Warehouse ETL Pipeline

## Project Overview

This project aims to implement high-grade data pipelines using Apache Airflow for Sparkify, a music streaming company. The goal is to automate and monitor their data warehouse ETL (Extract, Transform, Load) processes, making them dynamic, reusable, and easy to backfill. Additionally, data quality checks will be incorporated to ensure the integrity of the datasets.

The source data is stored in Amazon S3 and needs to be processed and loaded into Sparkify's data warehouse hosted on Amazon Redshift. The source datasets include JSON logs containing user activity information and JSON metadata describing the songs users listen to.

## Local Execution

This project uses Airflow. Please follow the instructions [here](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html) in order to run Airflow using the docker-compose file on your local machine.

## Initial Setup

