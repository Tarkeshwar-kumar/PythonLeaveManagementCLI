from clint.textui import puts, colored
options = {
    "A": "Raise a request",
    "B": "Leave the application"
}

def display_options() -> None:
    for option in options:
        puts(colored.blue(option+ " -> "+ options[option]))
    user_action()
    
def user_action():
    option = input()
    if option == 'A':
        form = create_form()

def create_form() -> dict:
    pass
