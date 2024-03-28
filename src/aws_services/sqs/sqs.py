import boto3
from exceptions.exceptions import SQSSendMessageError, SQSGetMessageError

queue_url = "https://sqs.ap-south-1.amazonaws.com/642916324385/lms_add_emp_queue"
sqs_client = boto3.client('sqs')

def submit_request(message) -> Exception:
    try:
        response = sqs_client.send_message(
            QueueUrl = queue_url,
            MessageBody = message
        )
    except:
        raise SQSSendMessageError("Your request couldn't be send, check message body")

def get_request() -> Exception:
    try:
        response = sqs_client.receive_message(
            QueueUrl = queue_url,
            MaxNumberOfMessages=1
        )
    except:
        raise SQSGetMessageError("Something went wrong")
