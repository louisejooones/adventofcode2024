import pandas as pd
from aocd import get_data

input = get_data(day=2, year=2024)

reports = [[int(x) for x in line.split()] for line in input.strip().split('\n')]

def calculate_diffs(list):
    diffs = []
    for i in range(1,len(list)):
        diffs.append(list[i] - list[i-1])
    return diffs

def is_safe(diffs):
    safe = True
    inc = diffs[0] >= 0
    for diff in diffs:
        if abs(diff) > 3 or diff == 0:
            safe = False
            break
        if (diff > 0) != inc:
            safe = False
            break
    return safe

safe_reports = 0

for report in reports:
    diffs = calculate_diffs(report)
    if is_safe(diffs):
        safe_reports += 1

print(safe_reports)