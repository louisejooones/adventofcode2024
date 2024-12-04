import pandas as pd
from aocd import get_data

input = get_data(day=4, year=2024)

lines = [line for line in input.strip().split('\n')]

line_length = len(lines[0])

ne = -line_length + 1
se = line_length + 1
sw = -ne
nw = -se

directions = [ne, se]

string = input.strip().replace('\n', '')

x_mas_count = 0

def check_for_char(indx, direction, char):
    new_index = indx + direction
    if indx % line_length == 0 and direction in [nw, sw]:
        return False
    if (indx + 1) % line_length == 0 and direction in [ne, se]:
        return False
    if 0 <= new_index < len(string) and string[new_index] == char:
        return True
    else:
        return False
    
for indx, char in enumerate(string):
    if char == 'A':
        if check_for_char(indx, ne, 'M'):
            if check_for_char(indx, -ne, 'S'):
                if check_for_char(indx, se, 'M'):
                    if check_for_char(indx, -se, 'S'):
                        x_mas_count += 1
                if check_for_char(indx, se, 'S'):
                    if check_for_char(indx, -se, 'M'):
                        x_mas_count += 1
        if check_for_char(indx, ne, 'S'):
            if check_for_char(indx, -ne, 'M'):
                if check_for_char(indx, se, 'M'):
                    if check_for_char(indx, -se, 'S'):
                        x_mas_count += 1
                if check_for_char(indx, se, 'S'):
                    if check_for_char(indx, -se, 'M'):
                        x_mas_count += 1

print(x_mas_count)