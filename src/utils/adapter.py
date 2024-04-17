from utils.mapping import features
from clint.textui import puts, colored
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