from pyfiglet import Figlet
from clint.textui import puts, colored

def welcome() -> None:
    f = Figlet(font='big')
    print(f.renderText('EMPLOYEE PORTAL'))
    puts(colored.blue('WELCOME TO LEAVE MANAGEMENT SYSTEM'))


if __name__ == "__main__":
    welcome()