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

    def action():
        pass

class Developer(Employee):
    def action():
        developer_action()

class Admin(Employee):
    def action():
        admin_choose_action()

class Manager(Employee):
    def action():
        manager_action()

class Unauthorised(Employee):
    def action():
        user_action()

class EmployeeFactory(ABC):
    @abstractclassmethod
    def create_employee():
        pass

class ManagerFactory(EmployeeFactory):
    def create_employee(email_id):
        return Manager(email_id)

class AdminFactory(EmployeeFactory):
    def create_employee(email_id):
        return Admin(email_id)

class DeveloperFactory(EmployeeFactory):
    def create_employee(email_id):
        return Developer(email_id)

class UnauthorisedUserFactory(EmployeeFactory):
    def create_employee(email_id):
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
    for feature in features[role]:
        puts(colored.blue(feature+ " -> "+ features[feature]))

def action(role):
    pass
