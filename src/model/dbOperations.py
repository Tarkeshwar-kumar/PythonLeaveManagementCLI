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

def get_leave_stats(email_address):
    try:
        result = connection.execute(
            text(f'SELECT * FROM LeaveStats WHERE emp_email="{email_address}";')
        )
    except:
        raise NotAuthoriseError('You are not authrised, please raise a request to register')
    else:
        pass

def apply_for_leave(leave_type, number_of_leaves, email_address):
    try:
        result = connection.execute(
            text(f'UPDATE LeaveStats SET applied={number_of_leaves} WHERE type="{leave_type}" and emp_email="{email_address}";')
        )
    except:
        pass
    else:
        pass