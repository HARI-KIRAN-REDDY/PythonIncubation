def main():
    if __name__ == '__main__':
        print('Q1 : ', dict_q1_1, dict_q1_2)
        print('Q3 : ', my_dict_q3)
        print('Q4 : ', my_dict_q4)
        print('Q5 : ', my_dict_q5[5], my_list_q5_keys, my_list_q5_values, my_dict_q5)
        print('Q7 : ', frequency_of_words("count the words in the sentence in"))

# Q1. WAP to create a dictionary of numbers mapped to their negative value for numbers from 1-5.
# The dictionary should contain something like this:
# Do with both with and without range based for loop. {1:-1,2:-2,3:-3….}
dict_q1_1 = {}
dict_q1_2 = {}
my_tuple_q1 = (1, 2, 3, 4, 5)
for i in range(1,6):
    dict_q1_1[i] = -i
    #dict_q1_1.__setitem__(i, -i)
for i in my_tuple_q1:
    dict_q1_2[i] = -i

# Q2. Check which of the following declarations will work
# d = {1=2, 2=3} --> will not work
d = {1:2, 2:3} # --> will work
# d = {1,2; 2, 3} --> will not work
d = {(1,2), (2,3)} # --> will work
#d =  { 'a' : 'A', 'b' :1, c : [1234]  --> will not work
d =  { 'a' : 'A', 'b' :1, 'c' : [1234] } # --> Will work
d =  dict ( [(1, 2), (2, 3)] ) # --> will work
d =  dict ( ((1, 2), (2, 3)) ) # --> will work
d =  dict ( ([1, 2], [2, 3]) ) # --> will work
d = dict ( x = 2, y = 3) # --> will work
#d = dict('x' = 2, 'y' = 3) --> will not work
#d = dict(1 = 2, 2 = 3) --> will not work

# Q3. Read help for zip and write a program that has two lists l1 = [1,2,3,4], l2 = [10,20,30,40]
#And converts them to a dictionary d containing { 1:10,2:20 …….}
my_list_q3_1 = [1, 2, 3, 4]
my_list_q3_2 = [10, 20, 30, 40]
my_zip_q3 = zip(my_list_q3_1, my_list_q3_2)
my_dict_q3 = dict(my_zip_q3)

# Q4. Use range based for loop to store all upper case alphabets and their corresponding ASCII
# values in the dictionary d.
# The result should be d = {‘A’: 65, ‘B’:66,…..}
my_dict_q4 = {}
for i in range(ord('A'), ord('Z') + 1):
    my_dict_q4[chr(i)] = i

# Q5. Create a mapping of number to word from 0-9. (0:’zero’……)
my_dict_q5 = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
              5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
# • Ask user for a single digit number and print the corresponding word format.
number_q5 = int(input('(For Q5)Enter a single digit number : '))
# • Print all keys of above dictionary
my_list_q5_keys = my_dict_q5.keys()
# • Print all Values of a dictionary
my_list_q5_values = my_dict_q5.values()
# • Print all Key and Value pairs of above dictionary

# Q7. WAF: frequency_of_words()
def frequency_of_words(s):
    #sample s = 'I am ok are you ok'
    words = s.split()
    #words = ['I', 'am', 'ok', 'are', 'you', 'ok']
    frequency = [0]*len(words)
    #frequncey = [0, 0, 0, 0, 0, 0]
    frequency_dict= dict(zip(words, frequency))
    #frequency_dict = ['I':0, 'am':0, 'ok':0, 'are':0, 'you':0, 'ok':0]
    for word in words:
        frequency_dict[word]+=1
    return frequency_dict
main()