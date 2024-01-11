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


