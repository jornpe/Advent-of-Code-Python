from itertools import groupby

with open("input.txt") as f:
    lines = [i.strip() for i in f]

highest = 0
occupied = {}

for line in lines:

    rowsLower = 0
    rowsUpper = 127
    colLower = 0
    colUpper = 7

    for c in line:
        match c:
            case 'F':
                rowsUpper -= int((rowsUpper - rowsLower) / 2) + 1
            case 'B':
                rowsLower += int((rowsUpper - rowsLower) / 2) + 1
            case 'L':
                colUpper -= int((colUpper - colLower) / 2) + 1
            case 'R':
                colLower += int((colUpper - colLower) / 2) + 1

    if rowsUpper in occupied:
        occupied[rowsUpper].append(colUpper)
    else:
        occupied[rowsUpper] = [colUpper]

for row, col in occupied.items():
    if len(col) != 8:
        print(row)

