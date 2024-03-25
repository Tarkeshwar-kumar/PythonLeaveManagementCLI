import mysql.connector as mysql
from data.Credentals import Credential
from data.Employee import Employee

#creating context manager for the sql
class MySQL():
    def __init__(self):
        self.conn = None
    def __enter__(self):
        self.conn = mysql.connect(
            host = "localhost",
            database = "Employees",
            user = "tarak",
            password = "learn_and_code"
        )
        return self.conn
    def __exit__(self, type, value, traceback):
        if self.conn: self.conn.close()


    

