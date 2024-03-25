from data.Credentals import Credential
from auth.authentication import authenticate_user
from exceptions.exceptions import NotAuthoriseError
from db.crud_operations import *
from clint.textui import puts, colored
from pyfiglet import Figlet
 
def get_user_credential():
    
    email = input(colored.yellow('Enter your email address: '))
    password = input(colored.yellow('Enter your password: '))
    credential = Credential(
        email_id = email,
        password = password
    )
    return credential

def create_employee():
    email = input(colored.yellow('Enter your email address: '))
    password = input(colored.yellow('Enter your password: '))
    first_name = input(colored.yellow('Enter your first name: '))
    middle_name = input(colored.yellow('Enter your middle name: '))
    last_name = input(colored.yellow('Enter your last name: '))
    
    employee = Employee (
        first_name= first_name,
        middle_name= middle_name,
        last_name= last_name,
        email= email
    )
    credential = Credential (
        email_id= email,
        password= password
    )
    return employee, credential

def Application() -> None:
    puts(colored.blue('WELCOME TO LEAVE MANAGEMENT SYSTEM'))
    puts(colored.red('Please login to access portal'))
    credential = get_user_credential()

    try:
        employee = authenticate_user(credential)  
    except NotAuthoriseError as exception:
        print(exception)
        employee, credential = create_employee()
        insert_employee(employee)
        insert_emp_credentials(credential)
    else:
        colored.green('Congratulations you are logged in')

    
if __name__ == "Application":
    print(__name__)
    f = Figlet(font='big')
    print(f.renderText('EMPLOYEE PORTAL'))
    Application()
