from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    input = [list(line) for line in f.read().split('\n')]

symbols = {}

for row, line in enumerate(input):
    for col, char in enumerate(line):
        if input[row][col] != '.' and not input[row][col].isdigit():
            symbols[(row, col)] = char


def checkAround(start: int, end: int, row: int) -> bool:
    for r in range(row - 1, row + 2):
        for c in range(start - 1, end + 2):
            if (r, c) in symbols:
                return True
    return False


def get_answer():
    values = []
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
                    if checkAround(startindex, col - 1, row):
                        values.append(int(digits))
                startindex = None
                digits = ''

    return sum(values)


answer = get_answer()

print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
