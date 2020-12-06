#!/usr/bin/python3

input_file = "input.txt"

seat_ids = []

with open(input_file) as f:
    for line in f:
        seat_id = 0
        for char in line:
            if char == 'F' or char == 'L':
                seat_id = seat_id << 1
            elif char == 'B' or char == 'R':
                seat_id = seat_id << 1
                seat_id = seat_id | 1
        seat_ids.append(seat_id)

missing_seat_ids = list(set(range(min(seat_ids), max(seat_ids)))
                        .difference(seat_ids))
print(missing_seat_ids)
