from airflow.providers.amazon.aws.hooks.redshift_sql import RedshiftSQLHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
import os

class CreateRedshiftTablesOperator(BaseOperator):
    """
    Custom Airflow operator to create Redshift tables by executing SQL statements
    stored in a file.
    """
    @apply_defaults
    def __init__(
        self,
        sql_file_path="/opt/airflow/plugins/helpers/create_tables.sql",
        *args, **kwargs):
        
        super(CreateRedshiftTablesOperator, self).__init__(*args, **kwargs)
        self.sql_file_path = sql_file_path

    def execute(self, context):
        # Read the SQL statements from the file
        self.log.info("Start creating redshift tables.")
        self.log.info(f"Currently running in {os.getcwd()}")
        sql_statements = ""
        with open(self.sql_file_path, 'r') as sql_file:
            sql_statement = sql_file.read()
            
        sql_statements = self.get_list_sql_statements(sql_statement)

        # Create a PostgresOperator for executing SQL statements
        redshift_sql_hook = RedshiftSQLHook(
            task_id=f"{self.task_id}_redshift_op",
            aws_conn_id=self.dag.default_args.get("aws_conn_id"),
            redshift_conn_id=self.dag.default_args.get("redshift_conn_id")
        )
        redshift_sql_hook.run(sql_statements,
                               autocommit=True)
    
    def get_list_sql_statements(self, sql_statement):
        """ 
        This function takes a string with a lot of sql statements and returns list of 
        single statements that can be executed.
        """
        return [statement.rstrip() for statement in sql_statement.split(";") if statement.rstrip() != ""]