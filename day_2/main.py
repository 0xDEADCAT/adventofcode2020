#!/usr/bin/python3

import re

# Define regex rules
get_min = re.compile(r'^\d+')
get_max = re.compile(r'(?<=-)\d+')
get_char = re.compile(r'(?<= )[a-z](?=:)')
get_password = re.compile(r'(?<=: )\w+$')

# Setup
input_file = 'input.txt'

valid = 0
valid2 = 0

# Read numbers from file to numbers list
with open(input_file) as f:
   for line in f:
    min = int(get_min.search(line).group())
    max = int(get_max.search(line).group())
    char = get_char.search(line).group()
    password = get_password.search(line).group()

    # Part 1
    occurrences = password.count(char)
    if occurrences >= min and occurrences <= max:
        valid += 1
    # Part 2
    char_appears = 0
    indexes = [i+1 for i, ch in enumerate(password) if ch == char]
    if min in indexes:
        char_appears += 1
    if max in indexes:
        char_appears += 1
    if char_appears == 1:
        valid2 += 1

print(valid)
print(valid2)