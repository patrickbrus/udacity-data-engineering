# Udacity Data Engineering Nanodegree - Project Solutions
Welcome to my repository of project solutions for the Udacity Data Engineering Nanodegree. This repository serves as a comprehensive showcase of the skills and knowledge I've acquired throughout the course. Each project, located in its respective subfolder, is a testament to the practical, real-world challenges of data engineering.

## Projects Overview
This repository is structured into several subfolders, each representing a distinct project within the Data Engineering Nanodegree:
1. project-data-warehouse: This project, titled "Sparkify Data Warehouse on AWS Redshift," involves building an ETL pipeline that extracts data from S3, stages it in Redshift, and transforms it into a set of dimensional tables for analytical purposes.

## Project: Data Warehouse (project-data-warehouse)
### Overview
The "Sparkify Data Warehouse" project is part of the Udacity Data Engineering Nanodegree. It entails developing a cloud-based data warehouse solution for Sparkify, a music streaming startup. The project's goal is to enable Sparkify's analytics team to gain insights into user behavior and song preferences.

### Technologies Used
- AWS S3: Data storage for song and log datasets.
- AWS Redshift: Data warehousing solution to store and analyze large-scale data.
- SQL: Structuring and querying data in Redshift.
- Python: Scripting the ETL pipeline.

### Project Structure
- **sql_queries.py:** Contains SQL queries for dropping, creating, and inserting into tables.
- **create_tables.py:** Script to set up the database schema.
- **etl.py:** Script to extract data from S3, load it into staging tables on Redshift, and insert it into the analytics tables.
- **aws.cfg:** Config file for AWS including settings for Readshift cluster.
- **dwh.cfg:** Config file used for writing data to Redshift cluster.
- **IaC.ipynb:** Jupyter notebook that spins up required AWS resources.
- **README.md:** Project documentation (this file).# udacity-data-engineering

## Project: STEDI Human Balance Analytics (project-stedi-human-balance-analytics)

### Overview
This project is centered around the STEDI Step Trainer, a novel hardware device developed by the STEDI team. This device is designed to aid users in performing STEDI balance exercises and is equipped with sensors to collect motion data. The accompanying mobile app, integral to the product, collects customer data and interacts with the device's sensors. This project aims to leverage the sensor data from the Step Trainer and the mobile app's accelerometer to train a machine learning model for real-time step detection, with a strong emphasis on user privacy and data utilization ethics.

### Technologies Used
- **AWS S3**: Data storage for customer, accelerometer, and step trainer datasets.
- **AWS Glue**: Data processing and ETL (Extract, Transform, Load) jobs for data sanitization and preparation.
- **AWS Athena**: Querying processed data in AWS Glue tables.
- **Python**: Scripting for AWS Glue jobs and data processing tasks.
- **SQL**: Structuring and querying data in AWS Glue and Athena.

### Project Structure
- `README.md`: Project documentation (this file).
- `figures/`: Contains all the screenshots of the datasets and architecture diagrams.
    - `accelerometer_landing.png`
    - `accelerometer_trusted.png`
    - `customer_curated.png`
    - `customer_landing.png`
    - `customer_trusted.png`
    - `machine_learning_curated.png`
    - `project_architecture.png`
    - `step_trainer_landing.png`
    - `step_trainer_trusted.png`
- `src/`: Source code for the project.
    - `python/`: Python scripts for AWS Glue jobs.
        - `accelerometer_landing_to_trusted.py`
        - `customer_landing_to_trusted.py`
        - `customer_trusted_to_curated.py`
        - `machine_learning_curated.py`
        - `step_trainer_landing_to_trusted.py`
    - `sql/`: SQL scripts for initial data structuring.
        - `accelerometer_landing.sql`
        - `customer_landing.sql`
        - `step_trainer_landing.sql`

### Additional Notes
- Ensure proper configuration and deployment of AWS resources for seamless data flow.
- Regularly update and maintain the scripts to adapt to new data structures or requirements.
- Validate data integrity and consistency through regular checks and balances in the pipeline.

## Project: Data Pipelines with Airflow

### Overview

A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.

They have decided to bring you into the project and expect you to create high grade data pipelines that are dynamic and built from reusable tasks, can be monitored, and allow easy backfills. They have also noted that the data quality plays a big part when analyses are executed on top the data warehouse and want to run tests against their datasets after the ETL steps have been executed to catch any discrepancies in the datasets.

The source data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consist of JSON logs that tell about user activity in the application and JSON metadata about the songs the users listen to.

### Technologies Used

- **Apache Airflow**: Orchestrates and schedules data pipeline workflows, enabling automation and monitoring.
- **Amazon Redshift**: Serves as the data warehouse for storing and querying processed data with high performance.
- **Amazon S3**: Stores source data in JSON format, providing scalable and durable object storage in the cloud.
- **Python**: Primary programming language used for building the data pipeline and its components, offering extensive libraries and tools for data manipulation and integration with AWS services.
- **SQL**: Used for data transformation, querying, and quality checks within the data pipeline, including filtering, aggregation, joining, and data quality assurance.


### Project Structure
- **dags:** This folder contains the Directed Acyclic Graphs (DAGs) that defines the Airflow pipeline.
- **plugins:** Contains helper functions, operators, and other code components necessary for building and executing the data pipeline.
- **docker-compose:** Includes configuration files for setting up the Airflow environment using Docker Compose.
- **requirements.txt:** Lists the Python packages and dependencies required for the project.