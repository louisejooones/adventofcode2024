import pandas as pd
from aocd import get_data
import re

input = get_data(day=3, year=2024)

matches = re.findall(r"mul\((\d+,\d+)\)", input)

muls = [match.split(",") for match in matches]

df = pd.DataFrame(muls, columns=["x", "y"])

df["mul"] = df["x"].astype(int) * df["y"].astype(int)

print(sum(df["mul"]))