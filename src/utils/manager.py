from clint.textui import puts, colored
import sys
from model.dbOperations import get_employee, get_leave_stats, approve_leave, reject_leave
from validators.validate import is_valid_leave_request

def manager_action(email_address):
    action = input(colored.yellow('Choose action'))
    if action  == 'A':
        employee_info = get_employee(email_address)
        puts(colored.blue(employee_info))
    elif action == 'B':
        email_address = input(colored.yellow('Enter email address of employee '))
        employee_info = get_leave_stats(email_address)
        puts(colored.blue(employee_info))
    elif action == 'C':
        email_address = input(colored.yellow('Enter email address of employee '))
        leave_id = input(colored.yellow('Enter leave id '))
        approve_leave(email_address, leave_id)
    elif action == 'D':
        email_address = input(colored.yellow('Enter email address of employee '))
        leave_id = input(colored.yellow('Enter leave id '))
        reject_leave(email_address, leave_id)
    else:
        puts(colored.blue("Choosen invalid option"))
        sys.exit()