from clint.textui import puts, colored
from model.dbOperations import get_employee, delete_employee
import sys
from utils.static_methods import AdminAction, PrivateAction
def admin_choose_action():
    action = input(colored.yellow('Choose action'))
    if action  == 'A':
        AdminAction.see_emp_details()
    elif action == 'B':
        AdminAction.see_emp_leave_stats()
    elif action == 'C':
        AdminAction.approve_leave()
    elif action == 'D':
        AdminAction.reject_leave()
    elif action == 'E':
        pass
    elif action == 'F':
        AdminAction.remove_user()
    elif action == 'G':
        AdminAction.revoke_leave()
    elif action == 'H':
        AdminAction.change_manager()
    elif action == 'I':
        AdminAction.refresh_leave_records()
    else:
        puts(colored.blue("Choosen invalid option"))
        sys.exit()
