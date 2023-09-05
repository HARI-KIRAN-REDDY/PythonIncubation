import random
def main():
    if __name__ == '__main__':
        # Q1
        print('Q1 Swap Strings : ', swap_strings(string_q1,string_q2))
        # Q2
        print('Q2 Print average : ', avg_lambda(my_list_q2))
        # Q3
        # Q4
        print('Q4 Get simple interest : ', get_si(20000, 24, 2))
        # Q5
        print('Q5 Get Compound interest : ', get_ci(20000, 24, 2))
        # Q6
        print('Q6 Get Q and R : ',get_q_r(divisor_q6, dividend_q6))
        # Q7
        print('Q7 Get hypotenuse of triangle : ', get_hyp(base_q7, height_q7))
        # Q8
        print('Q8 Convert seconds into day:hour:minute:second format', get_time(seconds_q8))
        # Q9,10,11
        print('Q 9, 10 & 11 - |python -version| |2 -2| |none|')

# Q1. WAP to input 2 strings and swap the strings
string_q1 = input('(For Q1)Enter String 1 :')
string_q2 = input('(For Q2)Enter String 2 :')
def swap_strings(s1, s2):
    s1, s2 = s2, s1
    return s1, s2


# 2. WAP to generate 4 random numbers in the range 0-26 and print their average
my_list_q2 = []
for i in range(4):
    my_list_q2.append(random.randint(0,27))
avg_lambda = lambda x: sum(x)/len(x)


# 3. WAP to generate and print a random capital alphabet.


# 4. WAF get_si() that takes Principle, Rate and Time as arguments and returns the Simple Interest.
def get_si(principle, rate, time):
    return rate*principle*time/100


# 5. WAP get_ci() that takes Principle, Rate and Time as arguments and returns the Compound Interest.
def get_ci(principle, rate, time):
    return principle * ( 1 + rate/100)**time - principle


# 6. WAP get_q_r() taking 2 numbers as parameters and returns the quotient and remainder in the form of a tuple.
divisor_q6 = int(input('(For Q6)Enter divisor to divide : '))
dividend_q6 = int(input('(For Q6)Enter dividend to divide : '))
my_list_q6 = [('q', 'r')]
def get_q_r(divisor, dividend):
    my_list_q6.append(dividend//divisor)
    my_list_q6.append(dividend%divisor)
    return tuple(my_list_q6)


# 7. WAP to find the length of hypotenuse of a right angled triangle, input the height and base from user.
base_q7 = int(input('(For Q7)Enter length of base of a right angle triangle : '))
height_q7 = int(input('(For Q7)Enter height of a triangle : '))
def get_hyp(base, height):
    return (base**2 + height**2)**1/2


# 8. WAP to input number of seconds and print in days, hours, minutes and seconds ex: input = 10000
# Output = 0 day 2 hour 46 minute 40 second
seconds_q8 = int(input('(For Q8)Enter number of seconds : '))
def get_time(seconds):
    time_q8 = ''
    time_q8 += str(seconds//86400) + ' days : '
    seconds -= 86400*(seconds//86400)
    time_q8 += str(seconds//3600) + ' hr : '
    seconds -= 3600*(seconds//3600)
    time_q8 += str(seconds//60) + ' min : '
    seconds -= 60*(seconds//60)
    time_q8 += str(seconds) + ' sec'
    return time_q8


# 9. Check your version of python interpreter without opening the interpreter
# (Which command needs to be used on the command line).
'''
python -version
'''

# 10. Find Output :
# 	X = 2
# 	X *= 3
# 	X = X%4
# 	Y = - X
# 	print(X,Y)
'''
2-2
'''
#
# 11. Find Output:
# def funct():
#     pass
# print(funct())
main()
