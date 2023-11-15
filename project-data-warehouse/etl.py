import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    Loads data from S3 into staging tables on Redshift.

    The function iterates over queries listed in `copy_table_queries` and
    executes them. Each query copies data from JSON files in S3 to the 
    respective staging table in the Redshift cluster.

    Parameters:
    cur: psycopg2 cursor object to execute queries on the database.
    conn: psycopg2 connection object to the database.

    Returns:
    None
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    Transforms data from staging tables and inserts it into analytics tables.

    This function iterates over `insert_table_queries`. Each query takes
    data from staging tables, transforms it, and inserts it into the 
    respective final table in the star schema for analytics.

    Parameters:
    cur: psycopg2 cursor object to execute queries on the database.
    conn: psycopg2 connection object to the database.

    Returns:
    None
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Main function to manage the ETL process.

    Connects to the Redshift cluster, loads data from S3 to staging tables,
    transforms and loads data into the final analytics tables, and then
    closes the connection to the database.

    Parameters:
    None

    Returns:
    None
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()