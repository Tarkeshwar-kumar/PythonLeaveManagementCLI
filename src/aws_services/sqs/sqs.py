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

def get_employee_request() -> Exception:
    try:
        response = sqs_client.receive_message(
            QueueUrl = queue_url,
            MaxNumberOfMessages=1
        )
        print(response)
    except:
        raise SQSGetMessageError("Something went wrong")
    else:
        return response


def delete_request_from_queue(receipt_handle):
    try:
        response = sqs_client.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )
        print(response)
    except:
        raise SQSGetMessageError("Something went wrong")
    else:
        return response
    