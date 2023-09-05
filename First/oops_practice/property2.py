class A:
    def __init__(self, a):
        self._a = a

    def set_a(self, a):
        self._a = a

    def get_a(self):
        return self._a

    _a = property(get_a, set_a)

a = A(0)
