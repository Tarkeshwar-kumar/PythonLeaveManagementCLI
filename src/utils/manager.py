from clint.textui import puts, colored
import sys
from model.dbOperations import get_employee, get_leave_stats, approve_leave, reject_leave
from validators.validate import is_valid_leave_request
from utils.adapter import AdminAction, PrivateAction
def manager_action(email_address):
    action = input(colored.yellow('Choose action'))
    if action  == 'A':
        AdminAction.see_emp_details()
    elif action == 'B':
        pass
    elif action == 'C':
        AdminAction.see_emp_leave_stats()
    elif action == 'D':
        AdminAction.approve_leave()
    elif action == 'E':
        AdminAction.reject_leave()
    elif action == 'D':
        AdminAction.approve_leave()
    elif action == 'E':
        AdminAction.reject_leave()
    elif action == "F":
        PrivateAction.modify_peronal_details()
    elif action == "G":
        PrivateAction.modify_address_details()
    else:
        puts(colored.blue("Choosen invalid option"))
        sys.exit()