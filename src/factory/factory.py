from abc import ABC, abstractclassmethod
from utils.developers import developer_action
from utils.admin import admin_choose_action
from utils.manager import manager_action
from utils.unauthorised import user_action

class Employee:
    def __init__(self, email_id) -> None:
        self.email_id = email_id

    def action(self):
        pass

class Developer(Employee):
    def action(self):
        print(self.email_id)
        developer_action(self.email_id)

class Admin(Employee):
    def action(self):
        admin_choose_action()

class Manager(Employee):
    def action(self):
        manager_action()

class Unauthorised(Employee):
    def action(self):
        user_action()

class EmployeeFactory(ABC):
    @abstractclassmethod
    def create_employee(self):
        pass

class ManagerFactory(EmployeeFactory):
    def create_employee(self, email_id):
        return Manager(email_id)

class AdminFactory(EmployeeFactory):
    def create_employee(self, email_id):
        return Admin(email_id)

class DeveloperFactory(EmployeeFactory):
    def create_employee(self, email_id):
        return Developer(email_id)

class UnauthorisedUserFactory(EmployeeFactory):
    def create_employee(self, email_id):
        return Unauthorised(email_id)