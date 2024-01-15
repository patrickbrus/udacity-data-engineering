from airflow.providers.amazon.aws.hooks.redshift_sql import RedshiftSQLHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadFactOperator(BaseOperator):

    ui_color = '#F98866'

    @apply_defaults
    def __init__(self,
                 sql_query,
                 table,
                 redshift_conn_id="redshift",
                 aws_credentials_id="aws_credentials",
                 *args, **kwargs):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.sql_query = sql_query
        self.table = table
        self.redshift_conn_id = redshift_conn_id
        self.aws_credentials_id = aws_credentials_id

    def execute(self, context):
        self.log.info('Start loading data into fact table...')
        
        redshift_sql_hook = RedshiftSQLHook(
            task_id=f"{self.task_id}_redshift_op",
            aws_conn_id=self.aws_credentials_id,
            redshift_conn_id=self.redshift_conn_id
        )
        redshift_sql_hook.run(f"INSERT INTO {self.table} {self.sql_query}",
                              autocommit=True)
