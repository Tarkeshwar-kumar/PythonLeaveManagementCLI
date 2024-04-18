from db.Employee import Employees, Credentials, session, connection
from exceptions.exceptions import NotAuthoriseError, NoSuchEmployeeError
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
        employee = result.fetchall()
        if not employee:
            raise NoSuchEmployeeError(f"There is no employee with email id {email_id}")
        else:
            return employee
        
def delete_employee(email_id : Credentials.email_id):
    try:
        result = connection.execute(
            text(f'DELETE FROM Employees WHERE email_address="{email_id}";')
        )
    except Exception as exception:
        print(exception)
    else:
        connection.commit()

def get_leave_record(email_address: Credentials.email_id):
    try:
        result = connection.execute(
            text(f'SELECT * FROM LeaveRecord WHERE emp_email="{email_address}";')
        )
    except:
        raise NotAuthoriseError('You are not authrised, please raise a request to register')
    else:
        leave_record = result.fetchall()
        if not leave_record:
            raise NoSuchEmployeeError(f"There is no record for employee with email id {email_address}")
        else:
            return leave_record

def apply_for_leave(email_address, leave_type, from_date, till_date):
    try:
        connection.execute(
            text(f'INSERT INTO LeaveRecord (type, status, from_date, till_date, emp_email) VALUES ("{leave_type}", "APPLIED", "{from_date}", "{till_date}", "{email_address}");')
        )
    except Exception as exception:
        print(exception)
    else:
        connection.commit()


def approve_leave(email_address, leave_type):
    try:
        connection.execute(
            text(f'UPDATE LeaveRecord SET status="APPROVED" WHERE type="{leave_type}" and emp_email="{email_address}";')
        )
    except Exception as exception:
        print(exception)
    else:
        connection.commit()

def reject_leave(email_address, leave_type):
    try:
        result = connection.execute(
             text(f'UPDATE LeaveRecord SET status="REJEC"TED WHERE type="{leave_type}" and emp_email="{email_address}";')
        )
    except Exception as exception:
        print(exception)
    else:
        connection.commit()

def cancel_leave(email_address, leave_type):
    try:
        connection.execute(
            text(f'UPDATE LeaveRecord SET status="CANCELLED" WHERE type="{leave_type}" and emp_email="{email_address}";')
        )
    except Exception as exception:
        print(exception)
    else:
        connection.commit()

def revoke_leave(email_address, leave_type, from_date, till_date):
    try:
        result = connection.execute(
            text(f'UPDATE LeaveRecord status="REVOKED" WHERE type={leave_type}, from_date={from_date} and status=\'APPROVED\'";')
        )
    except Exception as exception:
        print(exception)
    else:
        connection.commit() 

def get_leave_stats(email_address, leave_type):
    try:
        result = connection.execute(
            text(f'SELECT total, availed FROM LeaveStats WHERE emp_email="{email_address}" and type="{leave_type}";')
        )
        output = result.fetchall()
        print(output)
    except Exception as exception:
        print(exception)
    else:
        return output[0][0], output[0][1]

def refersh_leave_record():
    now = datetime.datetime.now()
    date_now = datetime.datetime(now.year, now.month, now.day)
    try:
        result = connection.execute(
            text(f'UPDATE LeaveRecord status="AVAILED" WHERE type=\'APPROVED\' and till_date>{date_now} and status=\'APPROVED\'";')
        )
    except Exception as exception:
        print(exception)
    else:
        connection.commit()