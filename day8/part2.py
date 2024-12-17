import pandas as pd
import numpy as np
from aocd import get_data

input_data = get_data(day=8, year=2024)
input_data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

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
            potential_antinodes = []

            x_diff = coords[i][0] - coords[j][0]
            y_diff = coords[i][1] - coords[j][1]

            

            for antinode in potential_antinodes:
                if 0 <= antinode[0] < grid.shape[0] and 0 <= antinode[1] < grid.shape[1]:
                    antinodes.append(antinode)  
    return antinodes

locs['antinodes'] = locs['coordinates'].apply(find_antinodes)

antinodes = set()
for antinode in locs['antinodes']:
    antinodes.update(antinode)

print(len(antinodes))