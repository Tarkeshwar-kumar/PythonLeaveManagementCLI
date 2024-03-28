from clint.textui import puts, colored
import json
from aws_services.sqs.sqs import submit_request
from exceptions.exceptions import SQSSendMessageError
import sys
options = {
    "A": "Raise a request",
    "B": "Leave the application"
}

def display_options() -> None:
    for option in options:
        puts(colored.blue(option+ " -> "+ options[option]))
    user_action()
    
def user_action():
    option = input()
    if option == 'A':
        create_form()
    elif option == 'B':
        sys.exit()
    else:
        print("WRONG INPUT")

def create_form() -> dict:
    email = input(colored.yellow('Enter your email address: '))
    password = input(colored.yellow('Enter your password: '))
    first_name = input(colored.yellow('Enter your first name: '))
    last_name = input(colored.yellow('Enter your last name name: '))
    position = input(colored.yellow('Enter your position in the organisation: '))
    flat_number = input(colored.yellow('Enter your flat number: '))
    sector = input(colored.yellow('Enter your resedential sector: '))
    city = input(colored.yellow('Enter your city name: '))
    state = input(colored.yellow('Enter your state name: '))
    country = input(colored.yellow('Enter your country name: '))

    employee_details = {
            "email": email,
            "password": password,
            "first_name": first_name,
            "last_name": last_name,
            "position": position,
            "flat_number": flat_number,
            "sector": sector,
            "city": city,
            "state": state,
            "country": country
        }
    json_emp_details = json.dumps(employee_details)
    # submit_request(json_emp_details)
    try:
        submit_request(json_emp_details)
    except SQSSendMessageError as error:
        puts(colored.red("Your request couldn't be send, check message body"))
    else:
        puts(colored.green("Your request have been submitted"))

