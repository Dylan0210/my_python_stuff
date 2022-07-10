import boto3


ec2 = boto3.client('ec2')

response = ec2.create_volume(
    AvailabilityZone='us-east-1a',
    Encrypted=True,
    Size=8,
    SnapshotId='snap-04ea5ac74922bbc77',
    VolumeType='gp2'
)

print(response)