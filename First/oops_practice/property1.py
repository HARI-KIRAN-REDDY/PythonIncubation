class A:
    def __init__(self, a = 0, b = 0):
        self.set_a(a)
        self._b = b

    def set_a(self, a):
        if isinstance(a, int):
            self._a = a
        else:
            self._a = 0
            print('Invalid argument passed to set \'a\', now \'a\' has been set to \'0\'')

    def get_a(self):
        return self._a

a = A('a')
a.set_a(9)
print(a.get_a())
a.set_a('a')
print(a.get_a())


