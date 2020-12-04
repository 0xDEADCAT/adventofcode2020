#!/usr/bin/python3

# CAUTION: In order for this code to work, two blank lines have to be inserted
# at the end of the input file!

import re

input_file = "input.txt"

passport_keywords = {"byr": False, "iyr": False, "eyr": False, "hgt": False,
                     "hcl": False, "ecl": False, "pid": False}
optional_keywords = {"cid": False}

# Define regex rules
get_keyword = re.compile(r'\w+(?=:)')

correct_passports = 0
incorrect_passports = 0

with open(input_file) as f:
    for line in f:
        line = line.strip()
        if not line:
            if all(value is True for value in passport_keywords.values()):
                correct_passports += 1
            else:
                incorrect_passports += 1
            passport_keywords = {"byr": False, "iyr": False, "eyr": False,
                                 "hgt": False, "hcl": False, "ecl": False,
                                 "pid": False}
        else:
            keywords = get_keyword.findall(line)
            for keyword in keywords:
                if keyword in passport_keywords:
                    passport_keywords[keyword] = True

print(f'Valid passports: {correct_passports}')
print(f'Invalid passports: {incorrect_passports}')
