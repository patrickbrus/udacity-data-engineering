import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Accelerometer Landing Node
AccelerometerLandingNode_node1701677954036 = (
    glueContext.create_dynamic_frame.from_options(
        format_options={"multiline": False},
        connection_type="s3",
        format="json",
        connection_options={
            "paths": ["s3://udacity-spark-aws-demo/accelerometer/landing/"],
            "recurse": True,
        },
        transformation_ctx="AccelerometerLandingNode_node1701677954036",
    )
)

# Script generated for node Customer Trusted
CustomerTrusted_node1701678032472 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://udacity-spark-aws-demo/customer/trusted/"],
        "recurse": True,
    },
    transformation_ctx="CustomerTrusted_node1701678032472",
)

# Script generated for node Join
Join_node1701678071634 = Join.apply(
    frame1=AccelerometerLandingNode_node1701677954036,
    frame2=CustomerTrusted_node1701678032472,
    keys1=["user"],
    keys2=["email"],
    transformation_ctx="Join_node1701678071634",
)

# Script generated for node Drop Fields
DropFields_node1701678274130 = DropFields.apply(
    frame=Join_node1701678071634,
    paths=[
        "birthday",
        "serialnumber",
        "sharewithpublicasofdate",
        "sharewithresearchasofdate",
        "registrationdate",
        "customername",
        "sharewithfriendsasofdate",
        "timestamp",
        "email",
        "lastupdatedate",
        "phone",
    ],
    transformation_ctx="DropFields_node1701678274130",
)

# Script generated for node Accelerometer Trusted
AccelerometerTrusted_node1701678106027 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1701678274130,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://udacity-spark-aws-demo/accelerometer/trusted/",
        "partitionKeys": [],
    },
    transformation_ctx="AccelerometerTrusted_node1701678106027",
)

job.commit()
