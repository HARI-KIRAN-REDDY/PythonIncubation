class Temp:
    def __init__(self, a):
        self.a = a
        self.b = 'hi User : ' + str(a)

    def __str__(self):
        return 'Id : '  + str(self.a)


temp = Temp(7)
print(str(temp))
print(temp.__str__())