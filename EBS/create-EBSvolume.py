import boto3


ec2 = boto3.client("ec2")

response = ec2.create_volume(
    AvailabilityZone='us-east-1a',
    Size=8,
    Encrypted=True,               
    VolumeType='gp2'
)

print(response)