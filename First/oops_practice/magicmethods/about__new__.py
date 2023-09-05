class Temp:
    def __new__(cls, *args, **kwargs):
        print('__new__() running')
        inst = object.__new__(cls)
        print(args)
        return inst
    def __init__(self, a):
        self.a = a
        print('__init__() running')



temp = Temp(7)