def file_print(filename):
    my_file = open(filename, 'r')
    for my_line in my_file:
        print(my_line, end='')
    my_file.close()


# Q1 Write a program in python that stores alphabets from a to z in a text file.
file_q1 = open('z_q1.txt', 'w')
for i in range(26):
    file_q1.write(chr(ord('a') + i))
file_q1.close()
file_print('z_q1.txt')

# Q2

# Q3
file_q2 = open('z_q2.txt', 'w')
file_q2.write('line with some characters')
file_q2.close()

file_q2 = open('z_q2.txt', 'r')
print(file_q2.tell())
print(file_q2.read(4))
print(file_q2.tell())
file_q2.close()
'''
0
line
4
'''

# Q4 Write a program to read a file and copy it into a new file
file_q1 = open('z_q1.txt', 'r')
file_q4 = open('z_q4.txt', 'w')
for line in file_q1:
    file_q4.write(line)
file_q4.close()
file_q1.close()
file_print('z_q4.txt')

# Q5 Write a program to read a file and copy the contents to a new file such that the case gets
# reversed. i.e. upper case becomes lower case and vice versa
file_q5_1 = open('z_q5_1.txt', 'w')
file_q5_1.write('aBcDe\nFgHi')
file_q5_1.close()

file_q5_1 = open('z_q5_1.txt', 'r')
file_q5_2 = open('z_q5_2.txt', 'w')

for line in file_q5_1:
    string = ''
    for character in line:
        string += character.swapcase()
    file_q5_2.write(string)
file_q5_1.close()
file_q5_2.close()
file_print('z_q5_2.txt')

# Q6 Write a program that take a file name as command line argument, opens it and then counts
# number of space characters in that file


# Q7 Modify the above program to count the occurrence of each symbol i.e. count of alphabet ‘a’,
# count of spaces, count of commas and so forth.


