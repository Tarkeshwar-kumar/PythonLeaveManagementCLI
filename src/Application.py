# from clint.textui import puts, colored
# from pyfiglet import Figlet
# from exceptions.exceptions import NotAuthoriseError
from db.Employee import Employees, Credentials, Address, LeaveRecord, session, Base, engine, Manager
# from auth.authentication import *
# from utils.adapter import choose_features
# from utils.mapping import *
import datetime

manager1 = Manager(
    first_name = "David",
    last_name = "Morin",
    email_address = "david@hp.com"
)
emp1 = Employees(
    first_name = "Tarak",
    last_name = "kumar",
    position = "Developer",
    email_address = "ktarkeshwar305@gmail.com"
)

leave1 = LeaveRecord(
    # type = "sick leave",
    # status = "APPLIED",
    # from_date = datetime.datetime(year=2024, month=4, day=10),
    # till_date = datetime.datetime(year=2024, month=4, day=20),
)

address1 = Address(
    flat_number = 38, 
    sector = 10,
    city = "Ujjain",
    state = "Ujjain",
    country = "India"
)



emp2 = Employees(
    first_name = "Chelsi",
    last_name = "Goyal",
    position = "Admin",
    email_address = "goyal@gmail.com"
)

leave2 = LeaveRecord(
    # type = "Casual leave",
    # status = "APPLIED",
    # from_date = datetime.datetime(year=2024, month=4, day=10),
    # till_date = datetime.datetime(year=2024, month=4, day=20),
)

address2 = Address(
    flat_number = 38, 
    sector = 10,
    city = "Ujjain",
    state = "Ujjain",
    country = "India"
)

cred1 = Credentials(
    email_id = "ktarkeshwar305@gmail.com",
    password = "12345"
)

cred2 = Credentials(
    email_id = "goyal@gmail.com",
    password = "12345"
)
# emp1.leave_status.append(leave1)
emp1.address.append(address1)
emp1.credential.append(cred1)
manager1.emp_id.append(emp1)

# emp2.leave_status.append(leave2)
emp2.address.append(address2)
emp2.credential.append(cred2)
manager1.emp_id.append(emp2)
session.add(emp1)
session.add(emp2)
session.add(manager1)
session.commit()

print(emp1)
print("manager - > ", emp1.manager_email)
print("emp2", emp2.manager_email)

# def get_credential() -> Credentials:
#     email = input(colored.yellow('Enter your email address: '))
#     password = input(colored.yellow('Enter your password: '))
#     credential = Credentials(
#         email_id = email,
#         password = password
#     )
#     return credential

# def welcome() -> None:
#     f = Figlet(font='big')
#     print(f.renderText('EMPLOYEE PORTAL'))
#     puts(colored.blue('WELCOME TO LEAVE MANAGEMENT SYSTEM'))

# def login() -> Credentials:
#     puts(colored.red('Please login to access portal'))
#     credential = get_credential()
#     authenticate(credential)

# def authenticate(credential : Credentials) -> None :
#     try:        
#         employee = authenticate_user(credential)  
#         position = get_role(credential.email_id)
#     except NotAuthoriseError as exception:
#         puts(colored.red('You are not authrised, please raise a request to register'))
#     else:
#         puts(colored.green(f'Congratulations you are logged in as {position}'))
#     finally:
#         choose_features(credential.email_id, position)


# welcome()
# login()
