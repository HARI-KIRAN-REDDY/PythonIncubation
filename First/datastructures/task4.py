# 1. Guess output of each slice:
# s = "Python is Object Oriented"
# 1. s[-1]
'''d'''
# 2. s[::-1]
'''It will reverse string'''
# 3. s[:-1]
'''Python is Object Oriente'''
# 4. s[1:1]
''''''
# 5. s[4:10]
'''on is '''

# Q2 What error do you see for following statements: s = "" print(s[1])
'''string index out of range'''

# Q3 Do you get any error for the following code, if not give the output: S= "Landry" print(s[1])
'''Error is : name s is not defined'''
'''# S and s --> case sensitive'''
# Find output of the following:
# a) s="a b cd"
#    print(len(s))
#    print(s[::2])
#    print(len(s[::2]))
'''
6
abc
3
'''
# b) s="a#b#c#d#"
# print(s.split())
# print(s.split("#"))
# l=s.split("#")
# s="$".join(l)
# print(s)
'''
['a#b#c#d#']
[a, b, c, d]
a$b$c$d
'''
# c) S="Landry"
# S=S[::-2][::-2]
# print(S)
'''yda'''
# d) print(1>2)
'''false'''
# e) print(4%2, 5%2, 2%5, sep=", ")
'''0, 1, 2'''
# f) s="abcba"
# s.upper().
# print(s)
# print(s.count("A"), end = " ,")
# print(s.count("A", 2,4) , end = " ,")
# print(s.count("a", 2,4) , end = " ,")
'''
ABCBA
0, 0, 0
'''
# Q5 WAP to input a string and remove all spaces from it
my_string_q5 = input('(For Q5) Enter a string : ')
# Approach 1
my_list_q5 = my_string_q5.split()
my_string_q5 = "".join(my_list_q5)
# Approach 2
my_string_q5 = my_string_q5.replace(' ', '')

# Q6 What does this symbol denote: []
'''LIST'''

# Q7 WAP to print all methods(functions/operations) available in a string
print(dir(str))

# Q8 Using the above method, get all methods available for str (strings) and join it into a space
# separated string. (use join and dir methods)
print(" ".join(dir(str)))

# Q10 WAP to input a string and replace all space with new lines (\n) and print again.
my_string_q10 = input('(For Q10) Enter a string : ')
print(my_string_q10.replace(" ", "\n"))

# Q11 WAP to input Complete name and split it into first and last name and print it.
# also print after reversing each
my_string_q11 = input('(For Q11) Enter your name : ')
print(" ".join([name[::-1] for name in my_string_q11.split(" ")][::-1]))

# Q12 WAP to input a string and split it into 2 halves. The string can be of any length
my_string_q12 = input('(For Q12) Enter your name : ')
print(my_string_q12[:len(my_string_q12)], ' ', my_string_q12[len(my_string_q12):])
