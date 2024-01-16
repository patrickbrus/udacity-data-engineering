from airflow.providers.amazon.aws.hooks.redshift_sql import RedshiftSQLHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 sql_query,
                 table,
                 truncate_table=True,
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.sql_query = sql_query
        self.table = table
        self.truncate_table = truncate_table

    def execute(self, context):
        self.log.info(f"Start loading data into dimension table {self.table}...")
        
        # Create a RedshiftSQL operator to run the query
        redshift_sql_hook = RedshiftSQLHook(
            task_id=f"{self.task_id}_redshift_op",
            aws_conn_id=self.dag.default_args.get("aws_conn_id"),
            redshift_conn_id=self.dag.default_args.get("redshift_conn_id")
        )
        
        self.log.info(f"Truncate table is set to {self.truncate_table}.")
        if self.truncate_table:
            self.log.info(f"Truncate table first before inserting data...")
            redshift_sql_hook.run(f"TRUNCATE TABLE {self.table}",
                                  autocommit=True)
            
        redshift_sql_hook.run(f"INSERT INTO {self.table} {self.sql_query}",
                              autocommit=True)
