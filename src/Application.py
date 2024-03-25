from data.Credentals import Credential
from auth.authentication import authenticate_user
from exceptions.exceptions import NotAuthoriseError
from db.crud_operations import *
 
def get_user_credential():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    credential = Credential(
        email_id = email,
        password = password
    )
    return credential

def create_employee():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    first_name = input("Enter your first name: ")
    middle_name = input("Enter your middle name: ")
    last_name = input("Enter your last name: ")
    
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
    print("WELCOME TO LEAVE MANAGEMENT SYSTEM")

    print("Please login to access portal")

    credential = get_user_credential()

    try:
        employee = authenticate_user(credential)
    except NotAuthoriseError as exception:
        print(exception)
        employee, credential = create_employee()
        insert_employee(employee)
        insert_emp_credentials(credential)
    else:
        print("Congratulations you are logged in")

    
if __name__ == "Application":
    Application()
