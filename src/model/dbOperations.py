from db.Employee import Employees, Credentials, session, connection
from exceptions.exceptions import NotAuthoriseError
from clint.textui import puts, colored
from sqlalchemy import text, Select
from validators.validate import get_leave_stats

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

def get_leave_record(email_address: Credentials.email_id):
    try:
        result = connection.execute(
            text(f'SELECT * FROM LeaveRecord WHERE emp_email="{email_address}";')
        )
    except:
        raise NotAuthoriseError('You are not authrised, please raise a request to register')
    else:
        pass

def apply_for_leave(email_address, leave_type, from_date, till_date):
    try:
        result = connection.execute(
            text(f'UPDATE LeaveRecord SET type={leave_type}, status="APPLIED", from_date={from_date}, till_date={till_date} and emp_email="{email_address}";')
        )
    except:
        pass
    else:
        pass

def approve_leave(email_address, leave_id):
    try:
        result = connection.execute(
            text(f'UPDATE LeaveStats SET total=total- applied, applied={0} WHERE type="{leave_id}" and emp_email="{email_address}";')
        )
    except:
        pass
    else:
        pass

def reject_leave(email_address, leave_id):
    try:
        result = connection.execute(
            text(f'UPDATE LeaveStats SET total=total- applied, applied={0} WHERE type="{leave_id}" and emp_email="{email_address}";')
        )
    except:
        pass
    else:
        pass

def cancel_leave(email_address, leave_type, from_date, till_date):
    try:
        result = connection.execute(
            text(f'UPDATE LeaveRecord SET status="CANCELLED" WHERE type={leave_type}, from_date={from_date} and status=\'APPLIED\'";')
        )
    except:
        pass
    else:
        pass

def revoke_leave(email_address, leave_type, from_date, till_date):
    try:
        result = connection.execute(
            text(f'UPDATE LeaveRecord status="REVOKED" WHERE type={leave_type}, from_date={from_date} and status=\'APPROVED\'";')
        )
    except:
        pass
    else:
        pass 

def get_leave_stats(email_address, leave_type):
    try:
        result = connection.execute(
            text(f'SELECT total, availed FROM LeaveStats WHERE emp_email="{email_address}" and type={leave_type};')
        )
    except:
        raise NotAuthoriseError('You are not authrised, please raise a request to register')
    else:
        pass