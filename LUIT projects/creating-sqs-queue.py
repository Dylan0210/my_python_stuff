import boto3

# calling the resource
sqs = boto3.resource('sqs')

# creating the queue
queue = sqs.create_queue(QueueName= 'Time')

# printing out the queue url
print(queue.url)
