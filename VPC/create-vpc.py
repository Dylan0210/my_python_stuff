import boto3

# create vpc
ec2 = boto3.client('ec2')

ec2.create_vpc(CidrBlock='10.0.0.0/16')

response = ec2.create_vpc(CidrBlock='10.0.0.0/16')

print(response) 