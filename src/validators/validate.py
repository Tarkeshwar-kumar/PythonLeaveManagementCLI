from model.dbOperations import get_leave_stats
def is_valid_leave_request(email_address, leave_applied, leave_type) -> bool:
    leave_total, leave_availed = get_leave_stats(email_address, leave_type)
    if leave_total- leave_availed > leave_applied:
        return True
    return False


def is_valid_manager() -> bool:
    pass