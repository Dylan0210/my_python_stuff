import boto3
import os
import glob

# delete multiple objects from s3 bucket

s3 = boto3.client("s3")
objects = s3.list_objects(Bucket = "dylan-boto3-bucket")["Contents"]


for object in objects:
    s3.delete_object(Bucket = "dylan-boto3-bucket", Key = object['Key'])
    print(object["Key"])