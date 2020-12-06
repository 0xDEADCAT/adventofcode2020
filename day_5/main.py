#!/usr/bin/python3

input_file = "input.txt"

max_seat_id = 0

with open(input_file) as f:
    for line in f:
        row_min = 0
        row_max = 127
        col_min = 0
        col_max = 7
        line = line.strip()
        for row_specifier in line[:7]:
            if row_specifier == 'F':
                row_max = (row_max + row_min) // 2
            elif row_specifier == 'B':
                row_min = (row_max + row_min + 1) // 2
        for col_specifier in line[7:]:
            if col_specifier == 'L':
                col_max = (col_max + col_min) // 2
            elif col_specifier == 'R':
                col_min = (col_max + col_min + 1) // 2
        seat_id = row_min * 8 + col_min
        if seat_id > max_seat_id:
            max_seat_id = seat_id

print(max_seat_id)
