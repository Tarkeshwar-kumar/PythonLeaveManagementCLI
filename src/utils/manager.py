from clint.textui import puts, colored
import sys


def manager_action():
    action = input(colored.yellow('Choose action'))
    if action  == 'A':
        pass
    elif action == 'B':
        pass
    elif action == 'C':
        pass
    elif action == 'D':
        pass
    elif action == 'E':
        pass
    elif action == 'F':
        pass
    elif action == 'G':
        pass
    else:
        puts(colored.blue("Choosen invalid option"))
        sys.exit()