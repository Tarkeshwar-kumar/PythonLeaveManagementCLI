from clint.textui import puts, colored
import sys
from model.dbOperations import get_employee, get_leave_stats

def choose_action():
    action = input(colored.yellow('Choose action'))
    if action  == 'A':
        email_address = input(colored.yellow('Enter email address of the employee to get information'))
        employee_info = get_employee(email_address)
        puts(colored.blue(employee_info))
    elif action == 'B':
        email_address = input(colored.yellow('Enter email address of the employee to get information'))
        employee_info = get_leave_stats(email_address)
        puts(colored.blue(employee_info))
    elif action == 'C':
        pass
    elif action == 'D':
        pass
    else:
        puts(colored.blue("Choosen invalid option"))
        sys.exit()