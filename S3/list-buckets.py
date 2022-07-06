# list buckets

import boto3

s3 = boto3.client("s3")

response = s3.list_buckets()

buckets = response["Buckets"]

print(len(buckets))

for bucket in buckets:
    print(bucket["Name"])