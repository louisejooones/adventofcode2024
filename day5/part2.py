import pandas as pd
from aocd import get_data

input = get_data(day=5, year=2024)

lines = [line for line in input.strip().split('\n')]

