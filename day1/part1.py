import pandas as pd
from aocd import get_data

input = get_data(day=1, year=2024)

lines = [line.split('   ') for line in input.strip().split('\n')]
print(lines)

first = sorted([int(line[0]) for line in lines])
second = sorted([int(line[1]) for line in lines])

df = pd.DataFrame({'first': first, 'second': second})
df['diff'] = (df['second'] - df['first']).abs()

print(sum(df['diff']))