import boto3

ec2 = boto3.resource('ec2', region = 'us-east-1')

def lambda_handler(event, context):
    instances = ec2.instances.filter(
        Filters = [
            {'Name': 'instance-state-name', 'Values': ['running']},
            {'Name': 'tag:ENV','Values':['DEV']}
        ]
    )
    
    for instance in instances:
        id=instance.id
        ec2.instances.filter(InstanceIds=[id]).start()
        print("These instances have been started: " + instance.id)

    return "success"