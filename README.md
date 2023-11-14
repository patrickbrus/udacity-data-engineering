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
