from db.Employee import Employees, Credentials, session, connection
from exceptions.exceptions import NotAuthoriseError
from clint.textui import puts, colored
from sqlalchemy import text, Select

def authenticate_user(credential: Credentials) -> Employees.position:
    try:
        result = connection.execute(
            text(f'SELECT * FROM Credentials WHERE email_id="{credential.email_id}" and password="{credential.password}";')
        )
        employee_id = result.fetchall()[0][3]
        result = connection.execute(
            text(f'SELECT position FROM Employees WHERE id={employee_id};')
        )
        role = result.fetchall()[0][0]
    except:
        raise NotAuthoriseError('You are not authrised, please raise a request to register')
    else:
        return role