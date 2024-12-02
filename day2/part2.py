from aocd import get_data

input = get_data(day=2, year=2024)

reports = [[int(x) for x in line.split()] for line in input.strip().split('\n')]

def calculate_diffs(lst):
    diffs = []
    for i in range(1, len(lst)):
        diffs.append(lst[i] - lst[i-1])
    return diffs

def is_safe(diffs):
    """
    Determines if the sequence of differences is safe.
    
    Parameters:
    diffs (list): List of differences.
    
    Returns:
    int: The index of the first unsafe difference, or -1 if all differences are safe.
    """
    inc = diffs[0] >= 0
    for indx, diff in enumerate(diffs):
        if abs(diff) > 3 or diff == 0 or (diff > 0) != inc:
            return indx
    return -1

def dampener(report, indx):
    if 0 <= indx < len(report):
        new_report = report[:indx] + report[indx+1:]
        diffs = calculate_diffs(new_report)
        if is_safe(diffs) == -1:
            return True
    return False

safe_reports = set()

for report in reports:
    diffs = calculate_diffs(report)
    unsafe_index = is_safe(diffs)
    if unsafe_index == -1 or dampener(report, unsafe_index) or dampener(report, unsafe_index-1) or dampener(report, unsafe_index+1):
        safe_reports.add(tuple(report))

print(len(safe_reports))