class InvalidCredentialsException(Exception):
    def __init__(self, message = 'Wrong Details entered'):
        super().__init__(message)
class IncompleteDetailsException(Exception):
    def __init__(self, message = 'Complete Details were not entered'):
        super().__init__(message)
class ZeroProductsInCartException(Exception):
    def __init__(self, message = 'No Products were added in cart'):
        super().__init__(message)

class NoSuchProductInCartException(Exception):
    def __init__(self, message = 'There is no such ty of product to add'):
        super().__init__(message)