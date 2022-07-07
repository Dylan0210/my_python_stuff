import boto3
import os
import glob

# upload multiple files to bucket

cwd=os.getcwd()

files = glob.glob(cwd+"/*.py")
for file in files:
    s3 = boto3.client("s3")
    response = s3.upload_file(
    Filename = file,
    Bucket = "dylan-boto3-bucket",
    Key = file.split("/")[-1]
    )
print(files)