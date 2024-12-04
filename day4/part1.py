import pandas as pd
from aocd import get_data

input = get_data(day=4, year=2024)

lines = [line for line in input.strip().split('\n')]

line_length = len(lines[0])

n = -line_length
ne = -line_length + 1
e = 1
se = line_length + 1
s = line_length
sw = line_length - 1
w = -1
nw = -line_length - 1

directions = [n, ne, e, se, s, sw, w, nw]

string = input.strip().replace('\n', '')

xmas_count = 0

def check_for_char(indx, direction, char):
    new_index = indx + direction
    if indx % line_length == 0 and direction in [nw, w, sw]:
        return False
    if (indx + 1) % line_length == 0 and direction in [ne, e, se]:
        return False
    if 0 <= new_index < len(string) and string[new_index] == char:
        return True
    else:
        return False

for indx, char in enumerate(string):
    if char == 'X':
        for direction in directions:
            if check_for_char(indx, direction, 'M'):
                if check_for_char(indx + direction, direction, 'A'):
                    if check_for_char(indx + direction * 2, direction, 'S'):
                        xmas_count += 1

print(xmas_count)