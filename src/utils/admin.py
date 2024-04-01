from clint.textui import puts, colored
from model.dbOperations import get_employee, delete_employee
import sys

def admin_choose_action():
    action = input(colored.yellow('Choose action'))
    if action  == 'A':
        email_address = input(colored.yellow('Enter email address of the employee to get information'))
        employee_info = get_employee(email_address)
        puts(colored.blue(employee_info))
    elif action == 'B':
        pass
    elif action == 'C':
        email_address = input(colored.yellow('Enter email address of the employee to remove employee'))
        delete_employee(email_address)
        puts(colored.blue("Employee removed"))
    else:
        puts(colored.blue("Choosen invalid option"))
        sys.exit()
