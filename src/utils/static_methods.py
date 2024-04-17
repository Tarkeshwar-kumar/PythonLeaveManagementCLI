from clint.textui import puts, colored
from model.dbOperations import get_employee, delete_employee, get_leave_record, approve_leave, reject_leave, revoke_leave, apply_for_leave, cancel_leave, get_leave_stats
from validators.validate import is_valid_leave_request
import datetime
class AdminAction():
    @staticmethod
    def see_emp_details():
        email_address = input(colored.yellow('Enter email address of the employee to get information'))
        employee_info = get_employee(email_address)
        print(employee_info)
    
    @staticmethod
    def see_emp_leave_record():
        email_address = input(colored.yellow('Enter email address of employee '))
        employee_info = get_leave_record(email_address)
        print(employee_info)

    @staticmethod
    def approve_leave():
        email_address = input(colored.yellow('Enter email address of employee '))
        leave_type = input(colored.yellow('Enter leave id '))
        approve_leave(email_address, leave_type)

    @staticmethod
    def reject_leave():
        email_address = input(colored.yellow('Enter email address of employee '))
        leave_type = input(colored.yellow('Enter leave id '))
        reject_leave(email_address, leave_type)

    @staticmethod
    def remove_user():
        email_address = input(colored.yellow('Enter email address of the employee to remove employee'))
        delete_employee(email_address)
        puts(colored.blue("Employee removed"))

    @staticmethod
    def refresh_leave_records():
        pass

    @staticmethod
    def revoke_leave():
        email_address = input(colored.yellow('Enter email address of employee '))
        leave_id = input(colored.yellow('Enter leave id '))
        revoke_leave(email_address, leave_id)

class PrivateAction():
    @staticmethod
    def see_personal_details(email_address):
        employee_info = get_employee(email_address)
        print(employee_info)

    @staticmethod
    def apply_for_leaves(email_address):
        leave_type = input(colored.yellow('Enter leave type '))
        from_date= input(colored.yellow('Enter starting date of leave (YYYY-MM-DD)'))
        till_date= input(colored.yellow('Enter till date of leave (YYYY-MM-DD)'))
        number_of_days_on_leave = find_diffence_in_days(till_date, from_date)
        if is_valid_leave_request(email_address, number_of_days_on_leave, leave_type):
            apply_for_leave(email_address, leave_type, from_date, till_date)
        

    @staticmethod
    def cancel_applied_leaves(email_address):
        leave_type = input(colored.yellow('Enter leave type to cancel'))
        cancel_leave(email_address, leave_type)

    @staticmethod
    def see_personal_leave(email_address):
        employee_info = get_leave_record(email_address)
        print(employee_info)

def find_diffence_in_days(till_date, from_date):
    from_year, from_month, from_date = from_date.split("-")
    till_year, till_month, till_date = till_date.split("-")

    till = datetime.date(int(till_year), int(till_month), int(till_date))
    start = datetime.date(int(from_year), int(from_month), int(from_date))

    print(till- start)

    return (till- start).days



