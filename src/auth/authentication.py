from db.Employee import Employees, Credentials, session, connection
from exceptions.exceptions import NotAuthoriseError
from clint.textui import puts, colored
from sqlalchemy import text, Select
import bcrypt

def authenticate_user(credential: Credentials) -> Employees.position:
    try:
        result = connection.execute(
            text(f'SELECT password FROM Credentials WHERE email_id="{credential.email_id}";')
        )
        password = result.fetchall()
        print(password)
        password = bytes.fromhex(password[0][0])
    except Exception:
        raise NotAuthoriseError('You are not authrised, please raise a request to register')
    else:
        if len(password) == 0 or not bcrypt.checkpw(credential.password, password):
            raise NotAuthoriseError('You are not authrised, please raise a request to register')
        else:
            print("Logged in!!!")
        
    
def get_role(email_id):
    try:
        result = connection.execute(
            text(f'SELECT position FROM Employees WHERE email_address="{email_id}";')
        )
        employee = result.fetchall()
        print(employee)
    except Exception as exception:
        print(exception)
    else:
        return employee[0][0]