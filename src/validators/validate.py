from model.dbOperations import get_leave_stats
from constants.constants import leave_type as leave_types, role
import sys
from exceptions.exceptions import InValidRequest

def is_valid_leave_request(email_address, leave_applied, leave_type) -> bool:
    if  is_validate_leave_type(leave_type) or is_leave_remaining(email_address, leave_type, leave_applied):
        print("You do not have enough remainig leave")
        return False
    return False


def validate_request(request) -> bool:
    if request['position'] in role:
        return True
    raise InValidRequest("Position is not invalid")

def is_validate_leave_type(leave_type):
    if leave_type not in leave_types:
        print("Enter valid leave type") 
        return False
    
def is_leave_remaining(email_address, leave_type, leave_applied):
    leave_total, leave_availed= get_leave_stats(email_address, leave_type)
    if int(leave_total)- int(leave_availed) > leave_applied:
        return True
    return False