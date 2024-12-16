import pandas as pd
from aocd import get_data

input_data = get_data(day=5, year=2024)

lines = [line for line in input_data.strip().split('\n')]

rules = sorted(lines[:lines.index('')], key=lambda x: x.split('|')[0])
rules = [rule.split('|') for rule in rules]

updates = lines[lines.index('')+1:]
updates = [update.split(',') for update in updates]

def check_rule(num1, num2, rule):
    return num1 == rule[0] and num2 == rule[1]

def check_left(num, item, rules):
    return sum([check_rule(item, num, rule) for rule in rules])

def check_right(num, item, rules):
    return sum([check_rule(num, item, rule) for rule in rules])

for update in updates:
    for i, item in enumerate(update):
        left_elements = update[:i]
        right_elements = update[i+1:]
        for element in left_elements:
            left_check_result = check_left(element, item, rules)
        for element in right_elements:
            right_check_result = check_right(element, item, rules)

full_order = []

unique_numbers = set(rules[0])

full_order.append(rules[0][0])
full_order.append(rules[0][1])

for num in unique_numbers:
    if num not in full_order:
        