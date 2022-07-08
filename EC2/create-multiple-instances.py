import boto3


ec2 = boto3.resource('ec2')

response = ec2.create_instances(
    ImageId="ami-0cff7528ff583bf9a",
    InstanceType='t2.micro',
    MaxCount= 3,
    MinCount= 3
)
print(response)