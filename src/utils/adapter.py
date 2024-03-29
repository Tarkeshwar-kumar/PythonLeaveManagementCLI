from utils.features import *
from clint.textui import puts, colored

def choose_features(role= "unauthorised"):
    if role == "Manager":
        display_options(manager_features)
    elif role == "Lead":
        display_options(lead_features)
    elif role == "Developer":
        display_options(developer_features)
    elif role == "Admin":
        display_options(lead_features)
    else:
        display_options(unothorised_features)

def display_options(features) -> None:
    for option in features:
        puts(colored.blue(option+ " -> "+ features[option]))