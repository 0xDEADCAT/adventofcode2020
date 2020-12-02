#!/usr/bin/python3

# Setup
input_file = 'input.txt'
numbers = []

# Read numbers from file to numbers list
with open(input_file) as f:
   for number in f:
    numbers.append(int(number))

print(numbers)

for num1 in numbers:
    for num2 in numbers:
        for num3 in numbers:
            if num1 + num2 + num3 == 2020:
                print(f'Numbers {num1} and {num2} and {num3}')
                print(num1 * num2 * num3)