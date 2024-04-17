from utils.mapping import features
from clint.textui import puts, colored
from model.dbOperations import get_employee, delete_employee, get_leave_record, approve_leave, reject_leave, revoke_leave
from validators.validate import is_valid_leave_request
from model.dbOperations import get_employee, get_leave_stats, apply_for_leave, cancel_leave
from factory.factory import DeveloperFactory, AdminFactory, ManagerFactory, UnauthorisedUserFactory
import sys

role_factory_mapping = {
    "Manager": ManagerFactory(),
    "Developer": DeveloperFactory(),
    "Admin": AdminFactory(),
    "Unauthorised": UnauthorisedUserFactory()
}

def choose_features(email, role="Unauthorised"):
    display_options(role)
    factory = role_factory_mapping[role]
    employee = factory.create_employee(email)
    employee.action()

def display_options(role) -> None:
    options = features[role]
    for feature in options:
        puts(colored.blue(feature+ " -> "+ options[feature]))