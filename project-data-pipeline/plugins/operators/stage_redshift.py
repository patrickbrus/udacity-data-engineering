from airflow.providers.amazon.aws.transfers.s3_to_redshift import S3ToRedshiftOperator
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class StageToRedshiftOperator(BaseOperator):
    ui_color = '#358140'

    @apply_defaults
    def __init__(self,
                 schema: str,
                 table: str,
                 s3_bucket: str="patrick-data-pipeline-bucket",
                 s3_key: str="log-data",
                 copy_options: list=[],
                 *args, **kwargs):

        super(StageToRedshiftOperator, self).__init__(*args, **kwargs)
        self.schema = schema
        self.table = table
        self.s3_bucket = s3_bucket
        self.s3_key = s3_key
        self.copy_options = copy_options

    def execute(self, context):
        self.log.info(f"Start copying data from s3://{self.s3_bucket}/{self.s3_key} to redshift table {self.table} in schema {self.schema}...")
        
        stage_events_to_redshift = S3ToRedshiftOperator(
            task_id=f"{self.task_id}_s3_to_redshift_op",
            schema=self.schema,
            table=self.table,
            redshift_conn_id=self.dag.default_args.get("redshift_conn_id"),
            aws_conn_id=self.dag.default_args.get("aws_conn_id"),
            s3_bucket=self.s3_bucket,
            s3_key=self.s3_key,
            copy_options=self.copy_options
        )
        stage_events_to_redshift.execute(context)