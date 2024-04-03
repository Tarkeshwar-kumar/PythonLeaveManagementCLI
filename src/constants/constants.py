leave_type = ["Sick Leave", "Casual Leave", "Marriage Leave", "Earned Leave"]
leave_status_type = ["Availed", "Applied", "Cancelled", "Revoked", "Granted"]
region = "ap-south-1"
account = "642916324385"
sqs_name = "lms_add_emp_queue"
sqs_endpoint = f"https://sqs.{region}.amazonaws.com/{account}/{sqs_name}"
