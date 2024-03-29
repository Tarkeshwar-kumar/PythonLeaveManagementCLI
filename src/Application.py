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
#     position = "Developer",
#     email_address = "ktarkeshwar305@gmail.com"
# )

# leave1 = LeaveStats(
#     type = "sick leave",
#     applied = 10,
#     total = 15,
# )

# address1 = Address(
#     flat_number = 38, 
#     sector = 10,
#     city = "Ujjain",
#     state = "Ujjain",
#     country = "India"
# )

# emp2 = Employees(
#     first_name = "Chelsi",
#     last_name = "Goyal",
#     position = "Admin",
#     email_address = "goyal@gmail.com"
# )

# leave2 = LeaveStats(
#     type = "Casual leave",
#     applied = 10,
#     total = 15,
# )

# address2 = Address(
#     flat_number = 38, 
#     sector = 10,
#     city = "Ujjain",
#     state = "Ujjain",
#     country = "India"
# )

# cred1 = Credentials(
#     email_id = "ktarkeshwar305@gmail.com",
#     password = "12345"
# )

# cred2 = Credentials(
#     email_id = "goyal@gmail.com",
#     password = "12345"
# )
# emp1.leave_status.append(leave1)
# emp1.address.append(address1)
# emp1.credential.append(cred1)

# emp2.leave_status.append(leave2)
# emp2.address.append(address2)
# emp2.credential.append(cred2)

# session.add(emp1)
# session.add(emp2)
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
        position = authenticate_user(credential)  
    except NotAuthoriseError as exception:
        puts(colored.red('You are not authrised, please raise a request to register'))
    else:
        puts(colored.green(f'Congratulations you are logged in as {position}'))
    finally:
        choose_features(position)


welcome()
login()
