# Sparkify Data Warehouse ETL Pipeline

## Project Overview

This project aims to implement high-grade data pipelines using Apache Airflow for Sparkify, a music streaming company. The goal is to automate and monitor their data warehouse ETL (Extract, Transform, Load) processes, making them dynamic, reusable, and easy to backfill. Additionally, data quality checks will be incorporated to ensure the integrity of the datasets.

The source data is stored in Amazon S3 and needs to be processed and loaded into Sparkify's data warehouse hosted on Amazon Redshift. The source datasets include JSON logs containing user activity information and JSON metadata describing the songs users listen to.

## Local Execution

This project uses Airflow. Please follow the instructions [here](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html) in order to run Airflow using the docker-compose file on your local machine.

## Initial Setup

1. Create S3 Bucket.
2. Copy data into S3 Bucket.

    ```bash
    aws s3 cp s3://udacity-dend/log-data/ s3://patrick-data-pipeline-bucket/log-data/ --recursive
    aws s3 cp s3://udacity-dend/song-data/ s3://patrick-data-pipeline-bucket/song-data/ --recursive
    aws s3 cp s3://udacity-dend/log_json_path.json s3://patrick-data-pipeline-bucket/
    ```
3. Create IAM user and attach the following policies:
    - AdministratorAccess
    - AmazonRedshiftFullAccess
    - AmazonS3FullAccess
4. Create security key for IAM user and save credentials.
5. Create Redshift role:

    ```bash
    aws iam create-role --role-name my-redshift-service-role --assume-role-policy-document '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "redshift.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }'
    ```
6. Provide full s3 access to redshift role:

    ```bash
    aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess --role-name my-redshift-service-role
    ```
7. Create Redshift cluster and choose the created role ***my-redshift-service-role***.

## Setting up Connections
- Connect Airflow and AWS with creating an aws credentials connection in Airflow (***aws_credentials***)
- Connect Airflow and Redshift with creating a redshift connection in Airflow (***redshift***)

## Implemented Operators

This project implements several custom operators for building data pipelines using Apache Airflow. These operators are designed to facilitate data extraction, transformation, and quality checks in a Redshift database.

### StageToRedshiftOperator

The `StageToRedshiftOperator` is responsible for loading JSON-formatted data from an S3 bucket into an Amazon Redshift database. It performs the following tasks:

- Creates and runs a SQL COPY statement based on the provided parameters.
- Parameters specify the S3 file location, target Redshift table, and credentials.
- Supports templated fields to load timestamped files based on execution time.

### LoadFactOperator

The `LoadFactOperator` is used for loading data into fact tables in Redshift. It accepts SQL queries and executes them against the target Redshift database. Key features include:

- Executing SQL queries for fact table loading.
- Supporting append-only functionality for massive fact tables.
- Specifying the Redshift connection and AWS credentials.

### LoadDimensionOperator

The `LoadDimensionOperator` is responsible for loading data into dimension tables in Redshift. It provides the following capabilities:

- Executing SQL queries for dimension table loading.
- Supporting both truncate-insert and append-only modes.
- Specifying the Redshift connection and AWS credentials.

### DataQualityOperator

The `DataQualityOperator` is designed for running data quality checks on the loaded data in Redshift. It offers the following features:

- Running SQL-based test cases to check data quality.
- Comparing the test results with expected outcomes.
- Raising exceptions and retries in case of mismatches.

### Usage

These operators can be utilized within your Airflow DAGs to create flexible and reliable data pipelines. Make sure to configure the required connections and credentials in Airflow's Connection UI for Redshift and S3.

For specific examples and usage instructions, please refer to the DAGs and Python scripts in the repository.

For more details on each operator, check the respective class documentation in the projects source code.



