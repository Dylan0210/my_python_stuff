import boto3

# upload a file to bucket 

s3 = boto3.client("s3")
response = s3.upload_file( 
    Filename = "upload.png", 
    Bucket = "dylan-boto3-bucket", 
    Key = "upload.png")

