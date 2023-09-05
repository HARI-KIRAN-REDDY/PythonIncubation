import random


def main():
    if __name__ == '__main__':
        # Q1
        print('Q1 - Printing 1 to 10\n', function_q1())
        # Q2
        print('Q2 - Printing 10 to 1\n', function_q2())
        # Q3
        print('Q3 - Printing elements at odd index\n', function_q3())
        # Q4
        print('Q4 - Printing Sum and avg of random numbers\n', function_q4())
        # Q5
        print('Q5 - Printing every element in string\n', function_q5())
        # Q6
        print('Q6 - Printing Asci of every element in string\n', function_q6())
        # Q7
        print('Q7 - Store Asci of every element into tuple\n', function_q7())
        # Q8
        print('Q8 - Print sum of odd numbers only\n', function_q8())
        # Q9
        print('Q9 - Find index of number in tuple \n', my_tuple_q9.index(number_q9))
        # Q10 & Q11
        print('Q10 & Q11 - Find sum of a list \n', sum(my_list_q10))
        # Q10 & Q11
        print('Q12 & Q13 - Factorial od a number \n', function_q12())
# Q1 Print numbers from 1 to 10 using for loop
def function_q1():
    output_q1 = ''
    for i in range(1, 11):
        output_q1 = output_q1 + str(i) + '\n'
    return output_q1


# Q2 Print numbers from 10 to 1 using for loop
def function_q2():
    output_q2 = ''
    for i in range(10, 0, -1):
        output_q2 = output_q2 + str(i) + '\n'
    return output_q2


# Q3 Print Elements at Odd indexes from a list (Using for loop)
my_list_q3 = [10, 11, 20, 21, 30, 31, 40, 41]


def function_q3():
    output_q3 = '['
    for i in range(len(my_list_q3)):
        if i % 2 == 1:
            output_q3 = output_q3 + str(my_list_q3[i]) + ', '
    return output_q3 + ']'


# Q4 Create a list of 5 random numbers and then print the list, sum of all numbers and average
my_list_q4 = []
def function_q4():
    for i in range(5):
        my_list_q4.append(random.randint(1, 1000))
    output_q4 = 'sum : ' + str(sum(my_list_q4)) + '\n avg : ' + str(sum(my_list_q4)/len(my_list_q4))
    return output_q4

# Q5 WAP to input a string and print individual characters in the string using for loop.
string_q5 = input('(For Q5)Enter a string : ')
def function_q5():
    output_q5 = ''
    for character in string_q5:
        output_q5 += character + '\n'
    return output_q5

# Q6 WAP to input a string and print the ASCII value of each character in the string.
string_q6 = input('(For Q6)Enter a string : ')
def function_q6():
    output_q6 = ''
    for character in string_q5:
        output_q6 += '\'' + character + '\' is : ' + str(ord(character))  + '\n'
    return output_q6

# Q7 WAP to input a string and store the ASCII value of each character in the tuple.
string_q7 = input('(For Q7)Enter a string : ')
def function_q7():
    output_q7 = []
    for character in string_q5:
        output_q7.append(ord(character))
    return tuple(output_q7)


# Q8 Write a function that takes a list of numbers from user as argument and returns the sum of only odd numbers
my_list_q8= []
for i in range(6):
    my_list_q8.append(int(input('(For Q8)Enter a number : ')))
def function_q8():
    output_q8 = 0
    for number in my_list_q8:
        output_q8 += (number % 2)*number
    return output_q8

# Q9 WAP to input a list of numbers and store in a tuple.
# Now input another number and print the index of this number in the tuple.
my_list_q9 = my_list_q8
my_tuple_q9 = tuple(my_list_q9)
print(my_list_q9, ' (For Q9)Enter a number from the list : ')
number_q9 = int(input())

# Q10&11 WAP to input 10 numbers repeatedly & print the sum of numbers
my_list_q10 = my_list_q8

# Q12&13 WAP to input a number and print all numbers from 1 till that number & print its factorial
number_q12 = int(input('(For Q12&13)Enter a number : '))
def function_q12():
    output_q12 = ''
    output_q13 = 1
    for number in range(1, number_q12):
        output_q12 += str(number) + ' * '
        output_q13 *= number
    return output_q12 + str(number_q12) + ' = ' + str(output_q13*number_q12)

main()
