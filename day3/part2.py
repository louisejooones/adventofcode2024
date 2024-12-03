import pandas as pd
from aocd import get_data
import re

input = get_data(day=3, year=2024)

matches = re.findall(r"mul\((\d+,\d+)\)", input)
muls = [match.split(",") for match in matches]
splits = re.split(r"mul\(\d+,\d+\)", input)

do_or_donts = []

do = True

def find_do_or_dont(i):
    print("i is ", i)
    print(splits[i])
    if i == 0:
        return "do"
    ls = re.findall(r"(do(?:n't)?)\(\)", splits[i])
    if len(ls)>0:
        print("found ", ls[-1])
        return ls[-1]
    else:
        return find_do_or_dont(i-1)
    
for i in range(0,len(muls)):
    do_or_donts.append(find_do_or_dont(i))

df = pd.DataFrame(muls, columns=["x", "y"])
df["do_or_dont"] = [1 if do_or_dont == "do" else 0 for do_or_dont in do_or_donts]

df["mul"] = df["x"].astype(int) * df["y"].astype(int) * df["do_or_dont"]

print(sum(df["mul"]))