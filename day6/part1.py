from aocd import get_data

data = get_data(day=6, year=2024)

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

def check_for_obstacle(indx, direction):
    new_index = indx + direction
    if indx % line_length == 0 and direction == w:
        return "leave"
    if (indx + 1) % line_length == 0 and direction == e:
        return "leave"
    if new_index < 0 and direction == n:
        return "leave"
    if new_index >= len(string) and direction == s:
        return "leave"
    if string[new_index] == "#":
        return "obstacle"
    if string[new_index] in [".", "^"]:
        return "clear"
    return "error"

start_index = string.index("^")
start_direction = n

def navigate(indx, direction):
    visited = set([indx])
    while True:
        status = check_for_obstacle(indx, direction)
        if status == "clear":
            indx += direction
            visited.add(indx)
        elif status == "obstacle":
            direction = rotate(direction)
        else:
            return visited
        
visited = navigate(start_index, start_direction)

print(len(visited))