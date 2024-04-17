from db.Employee import Employees, Credentials, session, connection
from exceptions.exceptions import NotAuthoriseError
from clint.textui import puts, colored
from sqlalchemy import text, Select
import datetime

def get_employee(email_id: Credentials.email_id):
    try:
        result = connection.execute(
            text(f'SELECT * FROM Employees WHERE email_address="{email_id}";')
        )
    except:
        raise NotAuthoriseError('You are not authrised, please raise a request to register')
    else:
        return result.fetchall()

def delete_employee(email_id : Credentials.email_id):
    try:
        result = connection.execute(
            text(f'DELETE FROM Employees WHERE email_address="{email_id}";')
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
        return result.fetchall()

def apply_for_leave(email_address, leave_type, from_date, till_date):
    try:
        result = connection.execute(
            text(f'UPDATE LeaveRecord SET type={leave_type}, status="APPLIED", from_date={from_date}, till_date={till_date} and emp_email="{email_address}";')
        )
    except:
        pass
    else:
        pass

def approve_leave(email_address, leave_type):
    try:
        result = connection.execute(
            text(f'UPDATE LeaveRecord SET status="APPROVED" WHERE type="{leave_type}" and emp_email="{email_address}";')
        )
    except:
        pass
    else:
        pass

def reject_leave(email_address, leave_type):
    try:
        result = connection.execute(
             text(f'UPDATE LeaveRecord SET status="REJEC"TED WHERE type="{leave_type}" and emp_email="{email_address}";')
        )
    except:
        pass
    else:
        pass

def cancel_leave(email_address, leave_type):
    try:
        result = connection.execute(
            text(f'UPDATE LeaveRecord SET status="CANCELLED" WHERE type="{leave_type}" and emp_email="{email_address}";')
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
            text(f'SELECT total, availed FROM LeaveStats WHERE emp_email="{email_address}" and type="{leave_type}";')
        )
        output = result.fetchall()
    except:
        raise NotAuthoriseError('You are not authrised, please raise a request to register')
    else:
        return output[0][0], output[0][1]

def insert_casual_leaves(email_address):
    try:
        result = connection.execute(
            text(f'INSERT INTO LeaveStats VALUES("Casual Leaves", 12, 0, "{email_address}");')
        )
    except:
        raise NotAuthoriseError('You are not authrised, please raise a request to register')
    else:
        pass 

def insert_sick_leaves(email_address):
    result = connection.execute(
        text(f'INSERT INTO LeaveStats VALUES("Sick Leave", 10, 0, "{email_address}");')
    )
    

def insert_parental_leaves(email_address):
    try:
        result = connection.execute(
            text(f'INSERT INTO LeaveStats VALUES("Parental Leave", 30, 0, "{email_address}");')
        )
    except:
        raise NotAuthoriseError('You are not authrised, please raise a request to register')
    else:
        pass

def refersh_leave_record():
    now = datetime.datetime.now()
    date_now = datetime.datetime(now.year, now.month, now.day)
    try:
        result = connection.execute(
            text(f'UPDATE LeaveRecord status="AVAILED" WHERE type=\'APPROVED\' and till_date>{date_now} and status=\'APPROVED\'";')
        )
    except:
        raise NotAuthoriseError('You are not authrised, please raise a request to register')
    else:
        pass