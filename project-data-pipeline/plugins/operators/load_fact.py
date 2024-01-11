from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadFactOperator(BaseOperator):

    ui_color = '#F98866'

    @apply_defaults
    def __init__(self,
                 sql_query,
                 conn_id="redshift",
                 *args, **kwargs):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.sql_query = sql_query
        self.conn_id = conn_id

    def execute(self, context):
        self.log.info('Start loading data into fact table...')
        
        postgres_hook = PostgresHook(
            task_id=f"{self.task_id}_postgress_hook",
            postres_conn_id=self.conn_id
        )
        postgres_hook.run(self.sql_query)
        
