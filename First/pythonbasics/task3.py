import math


def main():
    if __name__ == '__main__':
        # Q1
        print('Q1 - predicted output : 514')
        #Q2
        print('Q2 - Length of a string : ', len(string_q2))
        # Q3
        print('Q3 - Sum : ', number1_q3+number2_q3, ', Difference : ', abs(number1_q3-number2_q3))
        # Q4
        print('Q4 - predicted output : abde')
        # Q5
        print('Q5 - predicted output : abababab')
        # Q6
        print(('Q6 - ' + string_q6 + '\n')*number_q6)
        # Q7
        print('Q7 - predicted output : <class \'str\'> & 19')
        # Q8
        # Q9
        print('Q9 - Find square root : ', math.sqrt(number_q9))
        # Q10
        print('Q10 - Find avg of 4 numbers : ', sum(my_list_q10)/len(my_list_q10))
        # Q11
        print('Q11 - Using help fun to get to know about abs() : \n '
              'Help on built-in function abs in module builtins:\nabs(x, /)\n'
              'Return the absolute value of the argument.')
        # Q12
        print('Q12 - print(__name__) will result in print(__main__)')
# Question - 1 Predict Output
'''
s1 = "Hello"
s2 = "This is Python
print(len(s1), len(s2))
'''

# Question - 2 Wap Input to a String and print its length
string_q2 = input('(For Q2)Enter a string : ')

# Question - 3 WAP to input 2 numbers and print their sum and difference
number1_q3 = int(input('(For Q3)Enter a number : '))
number2_q3 = int(input('(For Q3)Enter a number : '))

# Question - 4 Predict Output
'''
s1 = 'ab'
s2 = 'de'
s3 = s1 + s2
print(s3)
'''

# Question - 5 Predict Output
'''
s1 = 'ab' *4
print(s1)
'''

# Question - 6 Print the string n times on the screen (Don't use loops)
string_q6 = input('(For Q6)Enter a string : ')
number_q6 = int(input('(For Q6)Enter a number : '))


# Question - 7 Predict Output
'''
s1 = 'Hello'
s2 = 'This is India'
s3 = s1 + '\n' + s2
print(type(s3))
print(len(s3))
'''

# Question - 9 Input a number and find square root
number_q9 = int(input('(For Q9)Enter a number to get square root of it : '))

# Question - 10 Find avg of 4 numbers
my_list_q10 = []
for i in range(4):
    my_list_q10.append(int(input('(For Q10)Enter a number : ')))

# Question - 11 Use help() to know about abs() in python
'''
help()
abs
'''

# Question - 12 print(__name__) in interpreter
'''
print(__name__)
'''
main()