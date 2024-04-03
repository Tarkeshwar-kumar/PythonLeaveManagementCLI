from utils.magging import features
from utils.admin import admin_choose_action
from utils.developers import developer_action
from utils.manager import manager_action
from utils.unauthorised import user_action
from clint.textui import puts, colored
from abc import ABC, abstractclassmethod

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
    
role_factory_mapping = {
    "Manager": ManagerFactory(),
    "Developer": DeveloperFactory(),
    "Admin": AdminFactory(),
    "Unauthorised": UnauthorisedUserFactory()
}

def choose_features(email, role):
    display_options(role)
    factory = role_factory_mapping[role]
    employee = factory.create_employee(email)
    employee.action()

def display_options(role) -> None:
    options = features[role]
    for feature in options:
        puts(colored.blue(feature+ " -> "+ options[feature]))

def action(role):
    pass
