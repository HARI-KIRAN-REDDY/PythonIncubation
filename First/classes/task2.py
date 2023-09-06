import re
my_common_string = 'Hello world, Let us <tag> learn more pyThOn\n new Python again version 0001 and 0003-versions'
# Q1 Write a regex(WAR) that matches the word ‘python’ case insensitive.
pattern_q1 = re.compile('(?i)python')
q1 = re.search(pattern_q1, my_common_string)

# Q2 WAR that matches any string of any length except newlines.
pattern_q2 = re.compile(r'[^\n]')
print(re.findall(pattern_q2, my_common_string))

# Q3 3. WAR that matches stings in the format ‘aaaabbbb’, where a denotes digit and b denotes non-digit symbols.
pattern_q3 = re.compile(r'[0-9]{4}[^0-9]{4}')


# Q4 WAR to match xx_xx_XX, where x = any alphabet; _ = any white space; X = any non-whitespace
pattern_q4 = re.compile('(?i)([a-z]{2}\\s){2}\\S{2}')

# Q5 WAR to match strings starting with 3 digit characters
pattern_q5 = re.compile(r'^[0-9]{3}')

# Q6 WAR to match individual characters which are now vowels
pattern_q6 = re.compile('(?i)[aeiou]')

# Q7 WAR that matches any 4 digit number.
pattern_q7 = re.compile(r'[0-9]{4}')

# Q8 WAR to match numbers with 6-10 digits.
pattern_q8 = re.compile(r'[0-9]{6,10}')

# Q9 WAR to match any lower case alphabet
pattern_q9 = re.compile(r'[a-z]')

# 10 WAR to match all strings of the form ABBBBBB; where B can repeat 0 or more times
pattern_q10 = re.compile(r'\AA.*')

# Q11 WAR to match all string ending in any of these three characters (., ?, !)
pattern_q11 = re.compile(r'[.?!]$')

# Q12 WAR to match and extract values of all 3 digit numbers
pattern_q12 = re.compile(r'\d{3}')
print(re.findall(pattern_q12, my_common_string))

# Q13 WAR to check if a string is a negative string i.e. If contains any of the words: not, no,
pattern_q13 = re.compile(r'\b(?:not|no)')

# Q14 WAR to extract XML tags
pattern_q14 = re.compile(r'(<.*>)')
