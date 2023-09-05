# Q1  Find expected output
#     l = [10,20,30,40]
#     itr = iter(l)
#     print(next(itr), next(itr))
#     itr = iter(l)
#     print(next(itr), next(itr))
"""     '''
        10 20
        10 20
        '''
"""
#     itr = [10,20,30,40].__iter__()
#     print(itr.__next__(), itr.__next__())
#     itr = reversed([10,20,30,40])
#     print(itr.__next__(), itr.__next__())
"""     '''
        10 20
        40 30
        '''
"""
#     itr1 = range(10,20)
#     itr2 = range(1,10,4)
#     print(next(itr1))
#     print(next(itr2))
#     itr3 = iter(itr1)
#     print(next(itr3))
#     print(next(itr2))
#     print(next(itr1))
"""     '''
        10
        1
        11
        5
        12
        '''
"""
# Q2 Which exception is raised upon reaching the last element of on iterable via its iterator.
'''StopIteration'''

# Q3 Name the two methods that are required for the iterator protocol.
'''__iter__(), __next__()'''

# Q4 Write a Function that takes a type or object or variable as argument and returns True or False
# depending on whether the argument is an iterable or not
def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

# Q5 Write a generator, that generates Fibonacci numbers. The function takes a number as argument
# and generates numbers less than or equal to that number.
def fibonacci(num):
    previous_i = 0
    present_i = 1
    while previous_i <= num:
        yield previous_i
        previous_i, present_i = [present_i, (present_i+previous_i)]

# Q6 Write a generator that takes a list and a predicate function (or lambda) as arguments and
# gives values after applying the lambda to the elements of the list.
# (The elements present in the list itself should not change)
def my_generator(my_list, my_predicate):
    for i in my_list:
        yield my_predicate(i)

'''
my_list = [1,2,4,5,7,8,9]
my_predicate = lambda x : x%2==0
my_output = my_generator(my_list, my_predicate)
for i in my_output:
    print(i)
'''