from clint.textui import puts, colored
import sys
from utils.static_methods import AdminAction
def manager_action(email_address):
    action = input(colored.yellow('Choose action'))
    if action  == 'A':
        AdminAction.see_emp_details()
    elif action == 'B':
        AdminAction.see_emp_leave_record()
    elif action == 'C':
        AdminAction.approve_leave()
    elif action == 'D':
        AdminAction.reject_leave()
    elif action == 'E':
        AdminAction.approve_leave()
    else:
        puts(colored.blue("Choosen invalid option"))
        sys.exit()