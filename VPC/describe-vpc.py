import boto3


# describes all vpc in account

ec2 = boto3.client("ec2")

vpcs = ec2.describe_vpcs()["Vpcs"]

for vpc in vpcs:
    print(vpc["VpcId"])