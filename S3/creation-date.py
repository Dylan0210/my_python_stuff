# get creation date of buckets

import boto3

s3 = boto3.client("s3")

s3.list_buckets()["Buckets"][0]["Name"]

creation_date=s3.list_buckets()["Buckets"][0]["CreationDate"]

creation_date.strftime("%d%m%y_%H:%M:%s")

for bucket in s3.list_buckets()["Buckets"]:
    print(bucket["Name"])
    print(bucket["CreationDate"])