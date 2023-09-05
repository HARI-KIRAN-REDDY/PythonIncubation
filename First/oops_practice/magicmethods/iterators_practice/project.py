class Car:
    _index = 0
    def __init__(self, color):
        self._index = Car._index
        self._name = 'BMW'
        self._color = color
        Car._index += 1
    def __iter__(self):
        return self
    def __next__(self):
        return Car._index

car1 = Car('Blue')
car2 = Car('Black')
car3 = Car('White')
car4 = Car('Grey')

for i in car1:
    print(i)