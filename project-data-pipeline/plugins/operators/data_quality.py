from airflow.providers.amazon.aws.hooks.redshift_sql import RedshiftSQLHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 sql_tests: dict,
                 redshift_conn_id: str="redshift",
                 aws_credentials_id: str="aws_credentials",
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.sql_tests = sql_tests
        self.redshift_conn_id = redshift_conn_id
        self.aws_credentials_id = aws_credentials_id

    def execute(self, context):
        self.log.info(f"Start data quality check...")
        
        redshift_sql_hook = RedshiftSQLHook(
            task_id=f"{self.task_id}_redshift_op",
            aws_conn_id=self.aws_credentials_id,
            redshift_conn_id=self.redshift_conn_id
        )
        
        for sql_test in self.sql_tests:
            test_query = sql_test["test_query"]
            expected_result = sql_test["expected_result"]
            result = redshift_sql_hook.get_first(test_query)
            
            if result[0] != expected_result:
                raise ValueError(f"Data quality check failed for query {test_query}.")
            
            self.log.info(f"Data quality check passed for query {test_query}.")
                