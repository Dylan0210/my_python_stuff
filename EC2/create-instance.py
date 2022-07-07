import boto3


ec2 = boto3.resource("ec2")

response = ec2.create_instances(ImageId="ami-0cff7528ff583bf9a",
    InstanceType="t2.micro",
    MaxCount=1,
    MinCount=1)

print(response)