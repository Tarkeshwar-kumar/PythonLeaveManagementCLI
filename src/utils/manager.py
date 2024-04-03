from clint.textui import puts, colored
import sys
from model.dbOperations import get_employee, get_leave_stats, approve_leave, reject_leave
from validators.validate import is_valid_leave_request
from utils.adapter import CommonAdminAction
def manager_action(email_address):
    action = input(colored.yellow('Choose action'))
    if action  == 'A':
        CommonAdminAction.see_emp_details()
    elif action == 'B':
        pass
    elif action == 'C':
        CommonAdminAction.see_emp_leave_stats()
    elif action == 'D':
        CommonAdminAction.approve_leave()
    elif action == 'E':
        CommonAdminAction.reject_leave()
    else:
        puts(colored.blue("Choosen invalid option"))
        sys.exit()