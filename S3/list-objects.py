# list objects in bucket

import boto3

s3 = boto3.client("s3")

bucket_name = "wk8pipeline"

response = s3.list_objects(
    Bucket=bucket_name
)

objects = response["Contents"]

print(len(objects))

for object in objects:
    print(object["Key"])
