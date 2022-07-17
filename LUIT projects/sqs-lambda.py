import json
import boto3
from datetime import datetime


def lambda_handler(event, context):
    
    now = datetime.now()                #current date and time
    date = "%m/%d/%Y"                   #date format
    current_time = now.strftime(date)
    message = "This message was sent: " + current_time

    sqs = boto3.client('sqs')

    sqs.send_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/501357120714/Time",
        MessageBody=json.dumps(current_time)
    )

    return {
        'statusCode': 200,
        'body': json.dumps(message)
    } 
