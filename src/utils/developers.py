from clint.textui import puts, colored
import sys

from utils.static_methods import PrivateAction

def developer_action(email_address):
    action = input(colored.yellow('Choose action '))
    if action  == 'A':
        PrivateAction.see_personal_details(email_address)
    elif action == 'B':
        PrivateAction.see_personal_leave(email_address)
    elif action == 'C':
        PrivateAction.apply_for_leaves(email_address)
    elif action == 'D':
        PrivateAction.cancel_applied_leaves(email_address)
    else:
        puts(colored.blue("Choosen invalid option"))
        sys.exit()