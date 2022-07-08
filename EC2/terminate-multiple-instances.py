import boto3


ec2 = boto3.client("ec2")

response = ec2.describe_instances()
data = response["Reservations"]

list = []

for instances in data:
     instance = instances["Instances"]
     for ids in instance:
        instance_id=ids["InstanceId"]
        list.append(instance_id)

print(ec2.terminate_instances(InstanceIds=list))