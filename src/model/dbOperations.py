from db.Employee import Employees, Credentials, session, connection
from exceptions.exceptions import NotAuthoriseError
from clint.textui import puts, colored
from sqlalchemy import text, Select



def get_employee(email_id: Credentials.email_id):
    try:
        result = connection.execute(
            text(f'SELECT * FROM Employees WHERE email_id="{email_id}";')
        )
    except:
        raise NotAuthoriseError('You are not authrised, please raise a request to register')
    else:
        pass

def delete_employee(email_id : Credentials.email_id):
    try:
        result = connection.execute(
            text(f'DELETE FROM Employees WHERE id="{email_id}";')
        )
    except:
        raise NotAuthoriseError('You are not authrised, please raise a request to register')
    else:
        pass

def get_leave_stats(email_id : Credentials.email_id):
    try:
        result = connection.execute(
            text(f'SELECT * FROM LeaveStats WHERE id="{email_id}";')
        )
    except:
        raise NotAuthoriseError('You are not authrised, please raise a request to register')
    else:
        pass

