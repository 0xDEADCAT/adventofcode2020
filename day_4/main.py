#!/usr/bin/python3

# CAUTION: In order for this code to work, two blank lines have to be inserted
# at the end of the input file!

import re

input_file = "input.txt"

passport_fields = {"byr": None, "iyr": None, "eyr": None, "hgt": None,
                   "hcl": None, "ecl": None, "pid": None}
optional_fields = {"cid": None}

# Define regex rules
get_field = re.compile(r'\w+(?=:)')
get_value = re.compile(r'(?<=:)(#\w+|\w+)')

validator = {"byr": re.compile(r'^(19[2-9]\d|200[0-2])$'),
             "iyr": re.compile(r'^(201\d|2020)$'),
             "eyr": re.compile(r'^(202\d|2030)$'),
             "hgt": re.compile(r'^((1[5-8]\d|19[0-3])|(59|6\d|7[0-6]))(?(2)cm)'
                               r'(?(3)in)$'),
             "hcl": re.compile(r'^#(\d|[a-f]){6}$'),
             "ecl": re.compile(r'^(amb|blu|brn|gr(y|n)|hzl|oth)$'),
             "pid": re.compile(r'^\d{9}$')}

correct_passports = 0
incorrect_passports = 0

with open(input_file) as f:
    for line in f:
        line = line.strip()
        if not line:
            if all(value is not None for value in passport_fields.values()):
                correct_passports += 1
            else:
                incorrect_passports += 1
            passport_fields = {"byr": None, "iyr": None, "eyr": None,
                               "hgt": None, "hcl": None, "ecl": None,
                               "pid": None}
        else:
            fields = get_field.findall(line)
            values = get_value.findall(line)
            for key, value in zip(fields, values):
                if key in passport_fields:
                    if validator[key].match(value):
                        passport_fields[key] = value

print(f'Valid passports: {correct_passports}')
print(f'Invalid passports: {incorrect_passports}')
