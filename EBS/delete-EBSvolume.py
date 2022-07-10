import boto3


ec2 = boto3.client('ec2')

response = ec2.delete_volume(VolumeId = "vol-09459a0c5de36f454")

print(response)
