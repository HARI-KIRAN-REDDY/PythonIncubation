from math import pi

# Q1. Find Output of following:
# class Student:
#     pass
# s = Student()
# s.name="Guido"
# s.age=62
# print(s.name)
# print(s.age)
'''
Guido
62
'''
# class Student:
#     pass
# s1 = Student()
# s1.name="Guido"
# s1.age=62
# s2 = Student()
# s2.name="Bjarne"
# s2.age=67
# print(s1.name, s1.age)
# print(s2.name, s2.age)
'''
Guido 62
Bjarne 67
'''

# Q2 For the Student class in above example, add constructor with 2 arguments for name and age, to set the name and
# age attributes. Create a student object, initialize it with some values and print its attributes.
'''
class Student:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
    def set_name(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age
    def get_age(self):
        return str(self.age)
    def get_name(self):
        return self.name
    def set_marks(self, marks_list):
        self.marks_list = marks_list

    def print_details(self):
        print('name:', self.name)
        print('age:', self.age)
        print('Average:', sum(self.marks_list)/5)

student1 = Student(age=18, name='x-men')
'''

# print(student1.get_name(), ':', student1.get_age())

# Q3 Find Output
# class Test:
#     def __init__(self):
#         print("Constructor")
#     def __del__(self):
#         print("Destructor")
# s1 = Test()
# s2 = Test ()
'''
Constructor
Constructor
Destructor
Destructor
'''
# class Test:
#     def __init__(self):
#         print("Constructor")
#     def __del__(self):
#         print("Destructor")
# s1 = Test()
# Test()
# s2 = Test()
# s3 = s1
# del(s1)
'''
Constructor
Constructor
Destructor
Constructor
Destructor
Destructor
'''
# Q4 Add a method set_marks(marks_ list), that takes a list of marks in 5 subjects
# and stores in a new attribute marks. Also add a method print_details(), to student class
# to print average of marks and all details of student. (Hint : average will be calculated
# as (total marks)/5 ) Test your class against the following code:
# if __name__ == "__main__":
#     s = Student("abc", 20)
#     s.set_marks([80,60,90,70,99])
#     s.print_details()
'''
name: abc
age: 20
Average: 79.8
'''

# Q5 Create a class Circle, that stores the radius and contains 2 methods:
# get_area, get_perimeter, which give the area and perimeter respectively of the circle.
'''Answer'''


# class Circle:
#     def __init__(self, radius):
#         self.set_radius(radius)
#     def set_radius(self, radius):
#         self.radius = radius
#     def get_area(self):
#         return str(pi*self.radius**2)
#     def get_perimeter(self):
#         return str(2*pi*self.radius)

# Q6. Create a class SelfManaged such that it keeps track of the number of objects currently
# alive. Create a class method get_current_count(), that gives the number of objects currently
# alive in memory.
'''Answer'''
'''
class Self_managed:
    number_of_objects = 0
    def __init__(self):
        Self_managed.number_of_objects += 1
    def __del__(self):
        Self_managed.number_of_objects -= 1
    @classmethod
    def get_current_count(cls):
        return cls.number_of_objects
'''

# Q7 Create a class BankAccount, which contains attributes balance and name, and methods
# deposit() and withdraw(), to add and deposit some money in account. the balance should be set
# to 0 in the constructor, and withdrawal should be allowed only if sufficient balance is there.
# Also overload the str method to allow printing the details directly.X
#
"""
class BankAccount:
    def __init__(self, name):
        self.balance = 0
        print('Hi, Creating bank account with name : ', name)
        self.name = name
        print('Bank account number assigned : ', id(self))
        self.account_number = id(self)

    def deposit(self, amount):
        if isinstance(amount, int):
            self.balance += amount
        else:
            print('Invalid Input')

    def withdraw(self, amount):
        if not isinstance(amount, int):
            print('Invalid input ')
            return
        if amount > self.balance:
            print('Insufficient Balance in your bank account')
        else:
            self.balance -= amount
            print('With drawl successful')

    def __str__(self):
        return 'name : ' + self.name + '\nAccount No : ' + str(self.account_number) + '\nAvailable Balance : ' + str(self.balance)
"""