# Q1 Predict Output
import math

S1 = "Hello"
S2 = "This is Python"
print(len(S1), len(S2))
'''5 14'''

# Q2 WAP to input a string and print its length
my_string_q2 = input('(For Q2)Enter string : ')
print(len(my_string_q2))

# Q3 WAP to input 2 numbers and print their sum and difference.
my_num_q3_1 = int(input('(For Q3)Enter first number : '))
my_num_q3_2 = int(input('(For Q2)Enter first number : '))
print('Sum : ', my_num_q3_2+my_num_q3_1)
print('diff : ', abs(my_num_q3_1-my_num_q3_2))

# Q4 Predict Output
s1 = 'ab'
s2 = 'de'
s3 = s1 + s2
print(s3)
'''abde'''

# Q5 Predict Output
s1 = 'ab' * 4
print(s1)
'''abababab'''

#   Q6 WAP to input a string s and a number n. Print the string n times on the screen,
#    each should appear in a separate line
my_string_q6 = input('(For Q6)Enter string : ') + '\n'
my_num_q6 = int(input('(For Q6)Enter first number : '))
print(my_string_q6 * my_num_q6)

# Q7 Predict Output,
s1 = 'Hello'
s2 = 'This is India'
s3 = s1 + '\n' + s2
print(type(s3))
print(len(s3))
'''
<class 'str'>
19
'''

# Q8 Find the name of function to find the square root.
print(dir(math.sqrt))

# Q9 WAP to input a number and print its square root ()
my_num_q9 = int(input('(For Q9)Enter first number : '))
print(math.sqrt(my_num_q9))

# Q10 WAP to input 4 numbers from user and print their average
my_list_q10 = []
for i in range(4):
    my_list_q10.append(int(input('(For Q10)Enter' + str(i) + 'number : ')))
print(sum(my_list_q10)/len(my_list_q10))

help()
'''
>>> abs
>>> quit()
'''
# 12. What is the output of this code when run from python interpreter.
# 	print(__name__)
'''__main__'''