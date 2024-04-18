from model.dbOperations import get_leave_stats
from constants.constants import leave_type as leave_types, role
import sys
from exceptions.exceptions import InValidRequest

def is_valid_leave_request(email_address, leave_applied, leave_type) -> bool:
    if  is_validate_leave_type(leave_type) and is_leave_remaining(email_address, leave_type, leave_applied):
        return True

def validate_request(request) -> bool:
    if request['position'] in role:
        return True
    raise InValidRequest("Position is not invalid")

def is_validate_leave_type(leave_type):
    if leave_type not in leave_types:
        raise InValidRequest("Enter valid leave type") 
    return True
    
def is_leave_remaining(email_address, leave_type, leave_applied):
    try:
        leave_total, leave_availed= get_leave_stats(email_address, leave_type)
    except Exception as exception:
        raise InValidRequest("Enter valid leave type")
    else:
        if int(leave_total)- int(leave_availed) > leave_applied:
            return True
        raise InValidRequest("You do not have enough remainig leave")