# Sequence Characters

# \d - Digit
# \D - Non-digit
# \s - white space
# \S - non-white space
# \w - alphanumeric value
# \W - non-alphanumeric value
# \b - space around words
# \A - start at word i.e. beginning of string
# \Z - ending of string
# + - 1 or more repetition of the preceding character
# * - 0 or more repetition of the preceding character
# ? - 0 or 1 of the preceding character
# {m} - Exactly m occurence
# {m,n} - Between m and n occurence
# \ - Escape character, for using special character
# . - matches any character except a new line
# ^ - match a given regular expression in the beginning of string
# $ - match a given regular expression in the end of string
# [...] - range of values like [a-z] - range becomes a - z
# [^...] - matches any character except the given range

import re

input_str = "Take up one idea. one idea at a time"
# Find two characters after letter 'o'
result = re.search(r'o\w\w', input_str)     # 2 \w - for matching 2 alphanumeric character after o
print(result.group())    # group() - Gives the exact string that matches the pattern
# O/P - one

result = re.findall(r'o\w\w', input_str)     # 2 \w - for matching 2 alphanumeric character after o
print(result)
# O/P - ['one', 'one']
# If there are no matches, it returns an empty list []

result = re.match(r'o\w\w', input_str)     # Match searches only at the beginning of string
                                            # and as one comes in b/w therefore, None
print(result)
# O/P - None

input_str = "Take up one 23 idea. one idea 45 at a time"
print(re.split(r'\d+', input_str))

input_str = "Take up one 23 idea. one idea 45 at a time"
print(re.sub(r'one', 'two', input_str))      # Substitute

result = re.findall(r'o\w+', input_str)     # \w+ - 1 or more alphanumeric characters
print(result)
# O/P - ['one', 'one']

result = re.findall(r'o\w*', input_str)     # \w* - 0 or more alphanumeric characters
print(result)
# O/P - ['one', 'one']

result = re.findall(r'o\w?', input_str)     # \w? - 0 or 1
print(result)
# O/P - ['on', 'on']

result = re.findall(r'o\w{1}', input_str)     # \w{1} - 1 characters after o
print(result)
# O/P - ['on', 'on']

result = re.findall(r'o\w{0, 4}', input_str)     # \w{0, 4} - 0-4 character
print(result)
# O/P - [] # No character matching 4 characters after o

input_str = "Take up 1-1-2019 one 23 idea. one idea 45 at a time 31-12-2019"
result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', input_str)
print(result)

result = re.findall(r'^T\w*', input_str)     # ^T\w - means Ta
print(result)
