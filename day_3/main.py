#!/usr/bin/python3

from functools import reduce

input_file = 'input.txt'

input_map = []
encountered_trees_list = [0] * 4
step_right = [1, 3, 5, 7]


with open(input_file) as f:
    for line in f:
        input_map.append(line.strip())

encountered_trees = 0
columns = len(input_map[0])
current_col = 0

for i, row in enumerate(input_map[1:]):
    for j in range(4):
        if row[((i+1) * step_right[j]) % columns] == '#':
            encountered_trees_list[j] += 1

current_col = 0
for i, row in enumerate(input_map[2::2]):
    current_col += 1
    current_col = current_col % columns
    if row[current_col] == '#':
        encountered_trees += 1

encountered_trees_list.append(encountered_trees)
print(encountered_trees_list)
print(reduce(lambda x, y: x*y, encountered_trees_list))
