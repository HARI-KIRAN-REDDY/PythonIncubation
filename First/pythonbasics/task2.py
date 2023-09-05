from functools import reduce


def main():
    if __name__ == '__main__':
        # Q1
        print('Q1 - Square : ', square_lambda(5))
        print('Q1 - Inverse : ', inverse_lambda(5))
        print('Q1 - Negate : ', negate_lambda(5))
        # Q2
        print('Q2 - Using reduce function : ', reduce(lambda a, b: max(a, b), my_list_q2))
        # Q3
        print('Q3 - Defining map_multiple function : ',
              map_multiple(functions_q3, my_list_q3))
        # Q4
        # Q5
        print('Q5 - Output : ', ans)
        # Q6
        print('Q6 - Using filter() to get only number : ',
              list(filter(lambda n: type(n) == type(0), my_list_q6)))
        # Q7
        print('Q7 - Convert Height into meters : ', list(map(convert_to_meter, my_list_q7)))
        # Q8
        print('Q8 - My own map function : ', list(my_map(convert_to_meter, my_list_q7)))


# Question-1 Lambdas (Behaviour assigning to a variable)
square_lambda = lambda n: n * n
inverse_lambda = lambda n: 1 / n
negate_lambda = lambda n: -n

# Question-2  reduce function and an appropriate lambda to find the maximum number in a list
my_list_q2 = [3, 6, 4, 8, 9]

# Question-3, map_multiple
functions_q3 = [square_lambda, inverse_lambda, negate_lambda]
my_list_q3 = [1, 2, 4]
def map_multiple(functions, sequence):
    my_list = []
    for my_function in functions:
        internal_list = []
        for i in range(len(sequence)):
            internal_list.append(my_function(sequence[i]))
        my_list.append(internal_list)
    return my_list


# Question -4, Predict Output for following code
'''
l = [10,30,50,30,10]
f = lambda x,y : x if x>y else y
print(reduce(f,l))
'''
# It will print maximum number in the sequence


# Question - 5, Find Output
functions_q5 = [lambda x: x ** 0.5, lambda x: 1 / x]
my_list_q5 = [1, 4, 16, 64]
ans = []
for num in my_list_q5:
    for function in functions_q5:
        ans.append(function(num))
# Note: result of "lambda x: x**0.05" will not be replicated as per Question in assignment sheet


# Question - 6
my_list_q6 = [1, 'a', '2', 3, 4, 'hi']

# Question - 7 Convert feet and inchest to meters
my_list_q7 = ['5ft6in', '5ft', '6ft2in', '12ft11in']
convert_to_meter = lambda height: int(height[0:height.index('ft')]) * 0.3048 + int(
    height[height.index('ft') + 2:height.index('in')]) * 0.0254 if 'in' in height else int(
    height[0:height.index('ft')]) * 0.3048


# Question - 8 write my_map function
def my_map(my_function, sequence):
    new_sequence = []
    for i in sequence:
        new_sequence.append(my_function(i))
    return new_sequence


main()

