from db.Connector import MySQL
from data.Employee import Employee
from data.Credentals import Credential

def insert_employee(employee: Employee):
    with MySQL() as connection:
        curr = connection.cursor()
        curr.execute(f"INSERT INTO Employees VALUES(\
                    0,\
                    {employee.first_name},\
                    {employee.middle_name},\
                    {employee.last_name},\
                    {employee.email}\
        );")
        connection.commit()

def update_employee():
    with MySQL() as connection:
        pass

def delete_employee():
    with MySQL() as connection:
        pass

def read_employee_details():
    with MySQL() as connection:
        pass

def insert_emp_credentials(credential: Credential):
    with MySQL() as connection:
        curr = connection.cursor()
        curr.execute(f'INSERT INTO Credentials VALUES(\
                    0,\
                    {credential.email_id},\
                    {credential.password}\
        );')
        connection.commit()

def update_emp_credentials():
    with MySQL() as connection:
        pass

def delete_emp_credentials():
    with MySQL() as connection:
        pass
