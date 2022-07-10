import boto3


ec2 = boto3.client('ec2')

response = ec2.delete_snapshot(SnapshotId='snap-03d7ddfff9ebefa19')

print(response)