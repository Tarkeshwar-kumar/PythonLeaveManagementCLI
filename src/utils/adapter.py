from utils.features import features
from utils.admin import admin_choose_action
from utils.developers import developer_action
from utils.manager import manager_action
from utils.unauthorised import user_action
from clint.textui import puts, colored
from abc import ABC, abstractclassmethod

class Action(ABC):
    @abstractclassmethod
    def action():
        pass

class Manager_action(Action):
    def action():
        admin_choose_action()

def choose_features(email, role):
    display_options(role)
    if role == "Manager":
        manager_action(email)
    elif role == "Developer":
        developer_action(email)
    elif role == "Admin":
        admin_choose_action(email)
    else:
        user_action()

def display_options(role) -> None:
    for feature in features[role]:
        puts(colored.blue(feature+ " -> "+ features[feature]))

def action(role):
    pass
