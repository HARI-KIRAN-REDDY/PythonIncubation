class Car:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    # def __str__(self):
    #     return str(self.num) + " returning via __str__"

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:

            raise Exception("Reached limit")

cars = Car()
print(iter(cars))
print(cars.__next__())
print("Hi")
for i in cars:
    print(i)

