class InvalidCredentialsException(Exception):
    def __init__(self, message = 'Wrong Details entered'):
        super().__init__(message)
class IncompleteDetailsException(Exception):
    def __init__(self, message = 'Complete Details were not entered'):
        super().__init__(message)