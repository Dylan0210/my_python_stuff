import boto3

ec2 = boto3.client("ec2")

response = ec2.delete_vpc(
    VpcId="vpc-0518076c550a444be"
    )

print(response)