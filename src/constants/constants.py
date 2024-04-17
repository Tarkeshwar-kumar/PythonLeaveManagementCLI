leave_type = ["Sick Leave", "Casual Leave", "Parental Leave"]
leave_status_type = ["AVAILED", "APPLIED", "CANCELLED", "REVOKED", "APPROVED"]
role = ["Developer", "Admin", "Manager", "Unauthorised"]
region = "ap-south-1"
account = "642916324385"
sqs_name = "lms_add_emp_queue"
sqs_endpoint = f"https://sqs.{region}.amazonaws.com/{account}/{sqs_name}"
