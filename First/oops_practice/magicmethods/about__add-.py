class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point is ( x : ' + str(self.x) + ', y : ' + str(self.y) + ').'
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
p1 = Point(5, 6)
p2 = Point(9, 11)
print(p1 + p2)
print(p1.__add__(p2))
