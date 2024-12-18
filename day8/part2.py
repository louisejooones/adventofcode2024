import pandas as pd
import numpy as np
from aocd import get_data

input_data = get_data(day=8, year=2024)

lines = [line for line in input_data.strip().split('\n')]

grid = np.array([list(line) for line in lines])

characters_in_lines = list(set(''.join(lines)) - {'.'})

locs = pd.DataFrame(characters_in_lines, columns=['character'])
locs['coordinates'] = locs['character'].apply(lambda x: list(zip(*np.where(grid == x))))

locs['no_of_pairs'] = locs['coordinates'].apply(lambda x: len(x) - 1)

def find_antinodes(coords):
    antinodes = []

    for i in range(len(coords) - 1):
        for j in range(i + 1, len(coords)):
            print(coords[i], coords[j])
            x_len = grid.shape[0]
            y_len = grid.shape[1]
            
            potential_antinodes = []

            x_diff = coords[i][0] - coords[j][0]
            y_diff = coords[i][1] - coords[j][1]


            max_diffs = max(x_len, y_len)+1

            for diff in range(-max_diffs, max_diffs + 1):
                if x_diff != 0 and y_diff != 0:
                    potential_antinodes.append((coords[i][0] + x_diff * diff, coords[i][1] + y_diff * diff))
                elif x_diff == 0:
                    potential_antinodes.append((coords[i][0], coords[i][1] + y_diff * diff))
                elif y_diff == 0:
                    potential_antinodes.append((coords[i][0] + x_diff * diff, coords[i][1]))
            
            for antinode in potential_antinodes:
                if 0 <= antinode[0] < x_len and 0 <= antinode[1] < y_len:
                    antinodes.append(antinode)
    return antinodes

locs['antinodes'] = locs['coordinates'].apply(find_antinodes)

antinodes = set()
for antinode in locs['antinodes']:
    antinodes.update(antinode)

print(len(antinodes))