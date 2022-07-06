# create s3 bucket

import boto3

client = boto3.client("s3")

client.create_bucket(Bucket="test-bucket-boto3")