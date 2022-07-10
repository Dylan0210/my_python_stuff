import boto3


ec2 = boto3.resource('ec2')

# create 3 intances for PROD
prod = ec2.create_instances(
    ImageId='ami-0cff7528ff583bf9a',
    InstanceType='t2.micro',
    MaxCount= 3,
    MinCount= 3,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name','Value': 'PROD'},
                {'Key': 'ENV','Value': 'PROD'}
            ]
        }
    ]
)

print(prod)
    
# create 3 instances for DEV
dev = ec2.create_instances(
    ImageId='ami-0cff7528ff583bf9a',
    InstanceType='t2.micro',
    MaxCount= 3,
    MinCount= 3,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name','Value': 'DEV'},
                {'Key': 'ENV','Value': 'DEV'}
            ]
        }
    ]
)

print(dev)