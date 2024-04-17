from clint.textui import puts, colored
from model.dbOperations import *
from validators.validate import is_valid_leave_request, validate_request
import datetime
from aws_services.sqs.sqs import get_employee_request, delete_request_from_queue
from db.Employee import Employees, Credentials, Address, LeaveRecord, session, Base, engine, Manager, LeaveStats
import json
from exceptions.exceptions import NoSuchEmployeeError, InValidRequest

class AdminAction():
    @staticmethod
    def see_emp_details():
        email_address = input(colored.yellow('Enter email address of the employee to get information'))
        try:
            employee_info = get_employee(email_address)
        except (NoSuchEmployeeError, NotAuthoriseError) as exception:
            print(exception)
        else:
            print(employee_info)
    
    @staticmethod
    def see_emp_leave_record():
        email_address = input(colored.yellow('Enter email address of employee '))
        try:
            leave_record = get_leave_record(email_address)
        except (NoSuchEmployeeError, NotAuthoriseError) as exception:
            print(exception)
        else:
            print(leave_record)

    @staticmethod
    def approve_leave():
        email_address = input(colored.yellow('Enter email address of employee '))
        leave_type = input(colored.yellow('Enter leave type '))
        try:
            approve_leave(email_address, leave_type)
        except (NoSuchEmployeeError, NotAuthoriseError) as exception:
            print(exception)
        else:
            print("Leave is approved")

    @staticmethod
    def reject_leave():
        email_address = input(colored.yellow('Enter email address of employee '))
        leave_type = input(colored.yellow('Enter leave id '))
        try:
            reject_leave(email_address, leave_type)
        except (NoSuchEmployeeError, NotAuthoriseError) as exception:
            print(exception)
        else:
            print("Leave is rejected")

    @staticmethod
    def remove_user():
        email_address = input(colored.yellow('Enter email address of the employee to remove employee'))
        try:
            delete_employee(email_address)
        except (NoSuchEmployeeError, NotAuthoriseError) as exception:
            print(exception)
        else:
            puts(colored.blue("Employee removed"))

    @staticmethod
    def refresh_leave_records():
        refersh_leave_record()

    @staticmethod
    def revoke_leave():
        email_address = input(colored.yellow('Enter email address of employee '))
        leave_id = input(colored.yellow('Enter leave id '))
        try:
            revoke_leave(email_address, leave_id)
        except (NoSuchEmployeeError, NotAuthoriseError) as exception:
            print(exception)
        else:
            puts(colored.blue("Leave revoked"))

    @staticmethod
    def check_request():
        request = get_employee_request()
        messages = request.get("Messages")
        if not messages:
            print("There is no request to process")
        else:
            process_request(request['Messages'][0]['ReceiptHandle'], request["Messages"][0]["Body"])
        
class PrivateAction():
    @staticmethod
    def see_personal_details(email_address):
        employee_info = get_employee(email_address)
        print(employee_info)

    @staticmethod
    def apply_for_leaves(email_address):
        leave_type = input(colored.yellow('Enter leave type '))
        from_date= input(colored.yellow('Enter starting date of leave (YYYY-MM-DD)'))
        till_date= input(colored.yellow('Enter till date of leave (YYYY-MM-DD)'))
        number_of_days_on_leave = find_diffence_in_days(till_date, from_date)
        if is_valid_leave_request(email_address, number_of_days_on_leave, leave_type):
            apply_for_leave(email_address, leave_type, from_date, till_date)
        

    @staticmethod
    def cancel_applied_leaves(email_address):
        leave_type = input(colored.yellow('Enter leave type to cancel'))
        cancel_leave(email_address, leave_type)

    @staticmethod
    def see_personal_leave(email_address):
        employee_info = get_leave_record(email_address)
        print(employee_info)

def find_diffence_in_days(till_date, from_date):
    from_year, from_month, from_date = from_date.split("-")
    till_year, till_month, till_date = till_date.split("-")

    till = datetime.date(int(till_year), int(till_month), int(till_date))
    start = datetime.date(int(from_year), int(from_month), int(from_date))

    return (till- start).days

def process_request(ReceiptHandle, request):
    print("A -> Create Employee")
    print("B -> Reject request")
    option = input("Choose option")
    if option == "A":
        try:
            json_request = json.loads(request)
            create_employee(json_request)
        except InValidRequest as exception:
            print("Invalid request")
            delete_request_from_queue(ReceiptHandle)
        except  Exception as err:
            print(err)
        else: 
            puts(colored.blue("User have been created"))
            delete_request_from_queue(ReceiptHandle)
    else:
        print("Request have been rejected") 
        delete_request_from_queue(ReceiptHandle)

def create_employee(request):
    address = create_address_details(request)
    employee = create_employee_detials(request)
    cred = create_credentials(request)

    employee.address.append(address)
    employee.credential.append(cred)

    session.add(employee)
    session.commit()

def create_employee_detials(message):
    validate_request(message)
    employee = Employees(
        first_name = message['first_name'],
        last_name = message['last_name'],
        position = message['position'],
        email_address = message['email']
    )
    return employee

def create_address_details(message):
    address = Address(
        flat_number = message['flat_number'],
        sector = message['sector'],
        city = message['city'],
        state = message['state'],
        country = message['country']
    )
    return address

def create_credentials(message):
    cred = Credentials(
        email_id = message['email'],
        password = message['password']
    )
    return cred

def create_manager(message):
    manager = Manager(
        first_name = message['first_name'],
        last_name = message['last_name']
    )
    return manager
