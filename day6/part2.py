from aocd import get_data

data = get_data(day=6, year=2024)
# data = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""

lines = [line for line in data.strip().split('\n')]

line_length = len(lines[0])

n = -line_length
e = 1
s = line_length
w = -1

directions = [n, e, s, w]

def rotate(direction):
    indx = directions.index(direction)
    return directions[(indx + 1) % 4]

string = data.strip().replace('\n', '')

def check_for_obstacle(indx, direction, strng):
    new_index = indx + direction
    if indx % line_length == 0 and direction == w:
        return "leave"
    if (indx + 1) % line_length == 0 and direction == e:
        return "leave"
    if new_index < 0 and direction == n:
        return "leave"
    if new_index >= len(strng) and direction == s:
        return "leave"
    if strng[new_index] == "#":
        return "obstacle"
    if strng[new_index] in [".", "^"]:
        return "clear"
    return "error"

start_index = string.index("^")
start_direction = n

def navigate(indx, direction, strng):
    visited = set()
    while True:
        if (indx, direction) in visited:
            return 1
        visited.add((indx, direction))

        status = check_for_obstacle(indx, direction, strng)
        if status == "clear":
            indx += direction
        elif status == "obstacle":
            direction = rotate(direction)
        else:
            return 0

loop_count = 0

for indx, char in enumerate(string):
    if char in ["#", "^"]:
        continue
    else:
        new_string = string[:indx] + "#" + string[indx + 1:]
        loop = navigate(start_index, start_direction, new_string)
        if loop == 1:
            loop_count += 1        

print(loop_count)