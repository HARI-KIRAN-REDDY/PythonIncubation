# Q1. Predict output of
#     a. print([i+j for i in "abc" for j in "def"])
#         a) [‘da’, ‘ea’, ‘fa’, ‘db’, ‘eb’, ‘fb’, ‘dc’, ‘ec’, ‘fc’].
#         b) [[‘ad’, ‘bd’, ‘cd’], [‘ae’, ‘be’, ‘ce’], [‘af’, ‘bf’, ‘cf’]].
#         c) [[‘da’, ‘db’, ‘dc’], [‘ea’, ‘eb’, ‘ec’], [‘fa’, ‘fb’, ‘fc’]].
#         d) [‘ad’, ‘ae’, ‘af’, ‘bd’, ‘be’, ‘bf’, ‘cd’, ‘ce’, ‘cf’].
'''d) [‘ad’, ‘ae’, ‘af’, ‘bd’, ‘be’, ‘bf’, ‘cd’, ‘ce’, ‘cf’]'''
#     b. print([i.lower() for i in "HELLO"])
#         a) [‘h’, ‘e’, ‘l’, ‘l’, ‘o’].
#         b) ‘hello’
#         c) [‘hello’].
#         d) Hello
'''a) [‘h’, ‘e’, ‘l’, ‘l’, ‘o’]'''
#     c. text = "Zero One Two Three Four Five Six Seven Eight Nine"
#     result = [word[0]+word[-1] for word in text.split()]
#     print(result)
'''['zo', 'Oe', 'To', 'Te', 'Fr', 'Fe', 'Sx', 'Sn', 'Et', 'Ne']'''
#     d. text = "Zero One Two Three Four Five Six Seven Eight Nine"
#     result = [word[0]+word[-1] for word in text.split() if word[0] > word[-1] ]
#     print(result)
'''[]'''
#     e. text = "bangalore : city with lakes and punctures"
#     result = [word for word in text.split() if word.startswith((‘a’,’e’,’I’,’o’,’u’)) ]
#     print(result)
'''['and']'''

# Q2. Convert to list comprehension
my_list_q2_1 = [i / 10 for i in [10, 20, 30, 40, 50]]
my_list_q2_2 = [i for i in range(10) if i ^ 1 != 0]
my_list_q2_3 = [len([char for char in 'aLphaBEts' if char in 'aeiouAEIOU'])]
my_list_q2_4 = [char.swapcase() for char in 'aLphaBEts']

# Q3. Consider a list of words:
# Write a loop to store the first character of each word in a list from the above list.
my_list_q3_1 = ['Python', 'Object', 'Oriented', 'Language']
my_list_q3_2 = [word[0] for word in my_list_q3_1]

# Q4. Input a string from user, create a list of only those words whose length is more than 5 characters
my_string_q4 = input('(For Q5)Input a string : ')
my_list_q4 = [word for word in my_string_q4.split() if len(word) >= 5]

# Q5. WAP to take a string as a command line argument and print whether it is palindrome or not.
my_string_q5 = input('(For Q5)Input a string : ')
print(my_string_q5 == my_string_q5[::-1])

# Q6. Find Output
'''True _ _ n o n _ _ o _ _'''

# Q7. Write a list comprehension to store the following in a list: [‘w’, ‘wo’, ‘wor’, ‘word’, ‘words’]
my_string_q7 = 'word'
my_list_q7_1 = [my_string_q7[0:i + 1] for i in range(len(my_string_q7))]

# Q8. WAP to input 2 string from command line and create a list of common words in both the strings

