from utils.mapping import features
from utils.admin import admin_choose_action
from utils.developers import developer_action
from utils.manager import manager_action
from utils.unauthorised import user_action
from clint.textui import puts, colored
from abc import ABC, abstractstaticmethod
from model.dbOperations import get_employee, delete_employee, get_leave_stats, approve_leave, reject_leave
from validators.validate import is_valid_leave_request
from model.dbOperations import get_employee, get_leave_stats, apply_for_leave

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
    @abstractstaticmethod
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
    
class AdminAction():
    @staticmethod
    def see_emp_details():
        email_address = input(colored.yellow('Enter email address of the employee to get information'))
        employee_info = get_employee(email_address)
        puts(colored.blue(employee_info))
    
    @staticmethod
    def see_emp_leave_stats():
        email_address = input(colored.yellow('Enter email address of employee '))
        employee_info = get_leave_stats(email_address)
        puts(colored.blue(employee_info))

    @staticmethod
    def approve_leave():
        email_address = input(colored.yellow('Enter email address of employee '))
        leave_id = input(colored.yellow('Enter leave id '))
        approve_leave(email_address, leave_id)

    @staticmethod
    def reject_leave():
        email_address = input(colored.yellow('Enter email address of employee '))
        leave_id = input(colored.yellow('Enter leave id '))
        reject_leave(email_address, leave_id)

    @staticmethod
    def remove_user():
        email_address = input(colored.yellow('Enter email address of the employee to remove employee'))
        delete_employee(email_address)
        puts(colored.blue("Employee removed"))

class PrivateAction():
    @staticmethod
    def see_personal_details(email_address):
        employee_info = get_employee(email_address)
        puts(colored.blue(employee_info))

    @staticmethod
    def apply_for_leaves(email_address):
        leave_type = input(colored.yellow('Enter leave type '))
        number_of_leaves = input(colored.yellow('Enter number of leaves '))
        if is_valid_leave_request(email_address):
            apply_for_leave(leave_type, number_of_leaves, email_address)

    @staticmethod
    def cancel_applied_leaves(email_address):
        leave_type = input(colored.yellow('Enter leave type to cancel'))
        apply_for_leave(email_address, leave_type, 0)

    @staticmethod
    def see_personal_leave(email_address):
        employee_info = get_leave_stats(email_address)
        puts(colored.blue(employee_info))

    @staticmethod
    def modify_peronal_details():
        pass

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