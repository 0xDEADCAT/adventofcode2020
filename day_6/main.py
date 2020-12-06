#!/usr/bin/python3

input_file = "input.txt"

sum = 0
answers = set()

with open(input_file) as f:
    for line in f:
        line = line.strip()
        if not line:
            sum += len(answers)
            answers = set()
        else:
            for char in line:
                answers.add(char)

print(sum)
