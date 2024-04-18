from clint.textui import puts, colored
import sys
from utils.static_methods import AdminAction, PrivateAction
def admin_choose_action():
    action = input(colored.yellow('Choose action'))
    if action  == 'A':
        AdminAction.get_emp_details()
    elif action == 'B':
        AdminAction.get_emp_leave_records()
    elif action == 'C':
        AdminAction.approve_leave()
    elif action == 'D':
        AdminAction.reject_leave()
    elif action == 'E':
        AdminAction.check_request()
    elif action == 'F':
        AdminAction.remove_user()
    elif action == 'G':
        AdminAction.revoke_leave()
    elif action == 'H':
        AdminAction.refresh_leave_records()
    else:
        puts(colored.blue("Choosen invalid option"))
        sys.exit()
