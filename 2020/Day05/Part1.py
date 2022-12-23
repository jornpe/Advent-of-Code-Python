from itertools import groupby

with open("input.txt") as f:
    lines = [i.strip() for i in f]

highest = 0

for line in lines:

    rowsLower = 0
    rowsUpper = 127
    colLower = 0
    colUpper = 7

    for c in line:
        if c == 'F':
            rowsUpper -= int((rowsUpper - rowsLower) / 2) + 1
        elif c == 'B':
            rowsLower += int((rowsUpper - rowsLower) / 2) + 1
        elif c == 'L':
            colUpper -= int((colUpper - colLower) / 2) + 1
        elif c == 'R':
            colLower += int((colUpper - colLower) / 2) + 1

    answer = (rowsLower * 8) + colUpper

    if answer > highest:
        highest = answer

print(highest)
