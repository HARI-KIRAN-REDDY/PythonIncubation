# Q1. Convert a Tuple t = (1,2,3,4,5) to a list
my_tuple_q1 = (1, 2, 3, 4, 5)
my_list_q1 = [my_tuple_q1]
print(type(my_list_q1))

# Q2 WAP to join a list and a tuple: L = [1,3,5,7] T = (8,6,4,2)
my_tuple_q2 = (8, 6, 4, 2)
my_list_q2 = [1, 3, 5, 7]
my_list_q2_output = my_list_q2 + [my_tuple_q2]

# Q3 What is difference between list and tuple
'''
#LIST -> MUTABLE, []
#TUPLE -> IMMUTABLE, ()
'''

# Q4 Print the list in reverse order
my_list_q4 = [1, 2, 3, 4, 5]
print(my_list_q4[::-1])

# Q5 Print Elements at Odd indexes from a list l = [10,11,20, 21,30, 31, 40, 41]
my_list_q5 = [10, 11, 20, 21, 30, 31, 40, 41]
print(my_list_q5[1::2])

# Q6 How many ways you can copy a list.
'''
l2 = l1 #This will not copy a list just points out to the id(l1)
l2 = l1.copy()
l2 = list(l1)
l2 = [x for x in l1]
'''

# Q7 Predict output
# n_list = ["Happy",[2,0,1,5]]
# print(n_list[0][1])
# print(n_list[1][3])
'''
a
5
'''

# Q8 Predict output
# odd = [2,4,6,8]
# odd[0] = 1
# print(odd)
# odd[1:4] = [3,5,7]
# print(odd)
'''
[1, 4, 6, 8]
[1, 3, 5, 7]
'''

# Q9 Write a program to input a string and print if it is palindrome or not
my_string_q9 = input('(For Q9)Enter a String : ')
print('Palindrome') if my_string_q9 == my_string_q9[::-1] else print('Not palindrome')

# Q10 Use the range method and create a tuple containing the following values: (20, 15, 10, 5)
my_tuple_q10 = ([number for number in range(20, 0, -5)])

# Q 11 WAP to convert string to list of characters
my_string_q10 = input('(For Q10)Enter a String : ')
my_list_q10 = [character for character in my_string_q10]
