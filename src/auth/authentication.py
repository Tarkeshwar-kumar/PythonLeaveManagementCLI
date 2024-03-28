from db.Employee import Employees, Credentials, session, connection
from exceptions.exceptions import NotAuthoriseError
from clint.textui import puts, colored
from sqlalchemy import text, Select

def authenticate_user(credential: Credentials) -> Employees:
    try:
        result = connection.execute(
            text(f"SELECT * FROM Credentials WHERE email_id={credential.email_id} and password={credential.password};")
        )
    except:
        raise NotAuthoriseError('You are not authrised, please raise a request to register')