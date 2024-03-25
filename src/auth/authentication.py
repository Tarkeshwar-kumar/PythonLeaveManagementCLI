from data.Credentals import Credential
from data.Employee import Employee
from db.Connector import MySQL
from exceptions.exceptions import NotAuthoriseError

def authenticate_user(cred: Credential) -> Employee:
    with MySQL() as connection:
        cur = connection.cursor()
        cur.execute(f"SELECT * from Credentials where email_id='{cred.email_id}' and password='{cred.password}';")
        result = cur.fetchall()
        print(result)
        if result == list([]):
            raise NotAuthoriseError("Please signup to access portal")