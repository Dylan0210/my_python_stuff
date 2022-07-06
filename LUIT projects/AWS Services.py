#Create a list of aws services using Python.

# The list should be empty initially

aws_services = [ ]
print(aws_services)
print(len(aws_services))


# Populate the list using insert and append.

aws_services.insert(0, 'CloudFormation')
aws_services.insert(1, 'CloudFront')
aws_services.append('S3')
aws_services.append('DynamoDB')
aws_services.append('VPC')


# Print the list and the length of the list.

print(aws_services)
print(len(aws_services))


# Remove two specific services from the list by index and by name.

del aws_services[0] 
aws_services.remove('CloudFront')


# Print the new list and the new length of the list.

print(aws_services)
print(len(aws_services))


# Add the two services back into list.

aws_services += ['EC2', 'Cloud9']

# Print the list and the length of the list to verify services where added back.

print(aws_services)
print(len(aws_services))
