import boto3

# deletes a single object from s3 bucket

s3 = boto3.client("s3")


response = s3.delete_object(Bucket = "dylan-boto3-bucket", 
    Key = "upload.png")
