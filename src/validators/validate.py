from model.dbOperations import get_leave_stats
from constants.constants import leave_type as leave_types
import sys

def is_valid_leave_request(email_address, leave_applied, leave_type) -> bool:
    if leave_type not in leave_types:
        print("Enter valid leave type") 
        return False
    leave_total, leave_availed= get_leave_stats(email_address, leave_type)
    if int(leave_total)- int(leave_availed) > leave_applied:
        return True
    print("You do not have enough remainig leave")
    return False


def is_valid_manager() -> bool:
    pass