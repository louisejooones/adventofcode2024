import pandas as pd
from aocd import get_data

input_data = get_data(day=5, year=2024)

lines = [line for line in input_data.strip().split('\n')]

rules = sorted(lines[:lines.index('')])
rules_df = pd.DataFrame(rules, columns=['rule'])

updates = lines[lines.index('')+1:]
updates_df = pd.DataFrame(updates, columns=['update'])

def check_rule(nums, rule):
    rule_list = rule.split('|')
    return nums.index(rule_list[0]) < nums.index(rule_list[1])

def switch_elements(nums, num1, num2):
    nums[nums.index(num1)], nums[nums.index(num2)] = nums[nums.index(num2)], nums[nums.index(num1)]
    return nums

def check_rules(nums, rules):
    return all([check_rule(nums, rule) for rule in rules])

def apply_rules(nums, rules):
    for rule in rules:
        rule_check = check_rule(nums, rule)
        if not rule_check:
            num1, num2 = rule.split('|')
            new_nums = switch_elements(nums, num1, num2)
            return apply_rules(new_nums, rules)
    return nums
           
def find_relevant_rule_for_num_pair(num1, num2):
    relevant_rule = rules_df[(rules_df['rule'] == f'{num1}|{num2}') | (rules_df['rule'] == f'{num2}|{num1}')]
    return relevant_rule['rule'].to_string(index=False).strip()

def find_relevant_rules_for_list_of_nums(nums):
    relevant_rules = []
    for i, num in enumerate(nums):
        for j in range(i+1, len(nums)):
            relevant_rules.append(find_relevant_rule_for_num_pair(num, nums[j]))
    return relevant_rules

def find_middle_num(nums):
    mid = len(nums) // 2
    if len(nums) % 2 == 0:
        return int(nums[mid-1:mid+1])
    else:
        return int(nums[mid])

updates_df['update_list'] = updates_df['update'].apply(lambda x: x.split(','))

updates_df['relevant_rules'] = updates_df.apply(lambda x: find_relevant_rules_for_list_of_nums(x['update_list']), axis=1)

updates_df['check_rules'] = updates_df.apply(lambda x: check_rules(x['update_list'], x['relevant_rules']), axis=1)

updates_df = updates_df[~updates_df['check_rules']]

updates_df['new_list'] = updates_df.apply(lambda x: apply_rules(x['update_list'], x['relevant_rules']), axis=1)

updates_df['middle_number'] = updates_df['new_list'].apply(lambda x: find_middle_num(x))

result = updates_df['middle_number'].sum()

print(updates_df)
print(result)