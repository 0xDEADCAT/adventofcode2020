#!/usr/bin/python3

input_file = "input.txt"

_sum = 0

with open(input_file) as f:
    groups = f.read().split('\n\n')
    for group in groups:
        group_answers = {}
        for answers in group.splitlines():
            for answer in answers:
                if answer in group_answers:
                    group_answers[answer] += 1
                else:
                    group_answers[answer] = 1
        num_of_persons = len(group.splitlines())
        _sum += sum(value == num_of_persons
                    for value in group_answers.values())

print(_sum)
