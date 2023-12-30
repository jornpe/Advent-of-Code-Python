from itertools import groupby

with open("input.txt") as f:
    lines = [i.strip() for i in f]

highest = 0
occupied = {}
ids = set()

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
        ids.add((rowsLower * 8) + colUpper)
    else:
        occupied[rowsUpper] = [colUpper]
        ids.add((rowsLower * 8) + colUpper)

answer = 0
for row, col in occupied.items():
    if len(col) != 8:
        for seat in [r for r in [0, 1, 2, 3, 4, 5, 6, 7] if r not in col]:
            seatid = row * 8 + seat
            if seatid - 1 in ids and seatid + 1 in ids:
                answer = seatid

print(f'⭐⭐ Part 2: {answer}')

