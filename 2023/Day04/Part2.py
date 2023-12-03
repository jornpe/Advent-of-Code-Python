from pathlib import Path

with open(Path(__file__).with_name('input.txt')) as f:
    input = [list(line) for line in f.read().split('\n')]

gears = {}

for row, line in enumerate(input):
    for col, char in enumerate(line):
        if input[row][col] == '*':
            gears[(row, col)] = []


def checkAround(start: int, end: int, row: int, digits: int):
    for r in range(row - 1, row + 2):
        for c in range(start - 1, end + 2):
            if (r, c) in gears:
                gears[(r, c)].append(digits)


def get_answer():
    for row, line in enumerate(input):
        digits = ''
        startindex = None

        for col, char in enumerate(line):
            if char.isdigit():
                digits += char
                if startindex is None:
                    startindex = col
            if not char.isdigit() or col == len(input[0]) - 1:
                if startindex is not None:
                    checkAround(startindex, col - 1, row, int(digits))
                startindex = None
                digits = ''

    return sum(x[0] * x[1] for x in [ratio for ratio in gears.values() if len(ratio) == 2])


answer = get_answer()

print(f'⭐⭐ Part 2: {answer}')
