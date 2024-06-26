from clint.textui import puts, colored
from pyfiglet import Figlet
from exceptions.exceptions import NotAuthoriseError
from db.Employee import Employees, Credentials, Address, LeaveRecord, session, Base, engine, Manager, LeaveStats
from auth.authentication import *
from utils.adapter import choose_features
from utils.mapping import *
import datetime
from getpass import getpass

def get_credential() -> Credentials:
    email = input(colored.yellow('Enter your email address: '))
    password = getpass(colored.yellow('Enter your password: '))
    password_encoded = password.encode('utf-8') 
    credential = Credentials(
        email_id = email,
        password = password_encoded
    )
    return credential

def welcome() -> None:
    f = Figlet(font='big')
    print(f.renderText('EMPLOYEE PORTAL'))
    puts(colored.blue('WELCOME TO LEAVE MANAGEMENT SYSTEM'))

def login() -> Credentials:
    puts(colored.red('Please login to access portal'))
    credential = get_credential()
    authenticate(credential)

def authenticate(credential : Credentials) -> None :
    position = "Unauthorised"
    try:        
        employee = authenticate_user(credential)  
        position = get_role(credential.email_id)
    except NotAuthoriseError as exception:
        puts(colored.red('You are not authrised, please raise a request to register'))
    else:
        puts(colored.green(f'Congratulations you are logged in as {position}'))
    finally:
        choose_features(credential.email_id, position)

if __name__ == "__main__":
    welcome()
    login()
