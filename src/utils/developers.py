from clint.textui import puts, colored
import sys
from model.dbOperations import get_employee, get_leave_stats, apply_for_leave
from validators.validate import is_valid_leave_request

def developer_action(email_address):
    action = input(colored.yellow('Choose action '))
    if action  == 'A':
        employee_info = get_employee(email_address)
        puts(colored.blue(employee_info))
    elif action == 'B':
        employee_info = get_leave_stats(email_address)
        puts(colored.blue(employee_info))
    elif action == 'C':
        leave_type = input(colored.yellow('Enter leave type '))
        number_of_leaves = input(colored.yellow('Enter number of leaves '))
        if is_valid_leave_request():
            apply_for_leave(leave_type, number_of_leaves)
    elif action == 'D':
        leave_type = input(colored.yellow('Enter leave type to cancel'))
        apply_for_leave(leave_type, 0)
    else:
        puts(colored.blue("Choosen invalid option"))
        sys.exit()