from aocd import get_data
import pandas as pd
from itertools import product

data = get_data(day=7, year=2024)

lines = [line for line in data.strip().split('\n')]

instructions = pd.DataFrame(lines, columns=['full'])

instructions['result'] = instructions['full'].str.split(':').str[0].astype(int)

instructions['number_string'] = instructions['full'].str.split(":").str[1].str.strip()

instructions['numbers'] = instructions['number_string'].str.split(" ").to_list()

def add(x,y):
    return x+y

def multiply(x,y):
    return x*y

instructions['number_count'] = instructions['numbers'].apply(len)

instructions['operation_count'] = instructions['number_count']-1

def list_options(operation_count):
    operations = [add, multiply]
    return [list(ops) for ops in product(operations, repeat=operation_count)]

instructions['options'] = instructions['operation_count'].apply(list_options)

def evaluate(numbers, operations):
    result = numbers[0]
    for i in range(len(operations)):
        result = operations[i](result, numbers[i+1])
    return result

def evaluate_all(numbers, options):
    return [evaluate(numbers, option) for option in options]

instructions['evaluations'] = instructions.apply(lambda x: evaluate_all([int(num) for num in x['numbers']], x['options']), axis=1)

instructions['match'] = instructions.apply(lambda x: x['result'] in x['evaluations'], axis=1)

instructions = instructions[instructions['match']==True]

sum = instructions['result'].sum()

print(sum)