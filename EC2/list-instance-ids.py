import boto3


ec2 = boto3.client("ec2")

response = ec2.describe_instances()

data = response["Reservations"][0]
data_instance = data["Instances"]

for i in range (len(data_instance)):
    print(f"instance id is {data_instance[i]['InstanceId']}")