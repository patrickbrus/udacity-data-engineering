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


