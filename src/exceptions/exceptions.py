
class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class NotAuthoriseError(CustomException):
    pass

class SQSSendMessageError(CustomException):
    pass

class SQSGetMessageError(CustomException):
    pass