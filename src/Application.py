from clint.textui import puts, colored
from pyfiglet import Figlet
from exceptions.exceptions import NotAuthoriseError
from db.Employee import Employees, Credentials, Address, LeaveStats, session, Base, engine
from auth.authentication import *
from utils.adapter import choose_features
from utils.features import *



# emp1 = Employees(
#     first_name = "Tarak",
#     last_name = "kumar",
# )

# leave1 = LeaveStats(
#     type = "sick leave",
#     applied = 10,
#     total = 15,
# )
# emp1.leave_status.append(leave1)

# session.add(emp1)
# session.commit()

# print(emp1)
# print(emp1.leave_status)

def get_credential() -> Credentials:
    email = input(colored.yellow('Enter your email address: '))
    password = input(colored.yellow('Enter your password: '))
    credential = Credentials(
        email_id = email,
        password = password
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
    try:        
        employee = authenticate_user(credential)  
    except NotAuthoriseError as exception:
        puts(colored.red('You are not authrised, please raise a request to register'))
    else:
        puts(colored.green(f'Congratulations you are logged in as {employee.position}'))
    finally:
        choose_features(employee.position)


welcome()
Base.metadata.create_all(engine)
login()
