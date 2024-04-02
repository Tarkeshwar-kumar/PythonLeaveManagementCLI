from utils.features import *
from utils.admin import admin_choose_action
from utils.developers import developer_action
from utils.manager import manager_action
from utils.unauthorised import user_action
from clint.textui import puts, colored

def choose_features(email, role= "unauthorised"):
    if role == "Manager":
        display_options(manager_features)
        manager_action(email)
    elif role == "Developer":
        display_options(developer_features)
        developer_action(email)
    elif role == "Admin":
        display_options(admin_features)
        admin_choose_action()
    else:
        display_options(unothorised_features)
        user_action()

def display_options(features) -> None:
    for option in features:
        puts(colored.blue(option+ " -> "+ features[option]))
