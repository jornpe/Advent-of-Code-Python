from pathlib import Path
import time
from pprint import pprint

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [list(line) for line in f.read().split('\n')]


def isXmas(pos: tuple, input: list) -> int:
    row, col = pos
    if row == 0 or row == len(input) - 1 or col == 0 or col == len(input) - 1:
        return 0
    first = [input[row - 1][col - 1], input[row][col], input[row + 1][col + 1]]
    second = [input[row + 1][col - 1], input[row][col], input[row - 1][col + 1]]
    if (first == ['M', 'A', 'S'] or first == ['S', 'A', 'M']) and (second == ['M', 'A', 'S'] or second == ['S', 'A', 'M']):
        return 1
    return 0


xmas = 0
for r, line in enumerate(lines):
    for c in [i for i, v in enumerate(line) if v == 'A']:
        xmas += isXmas((r, c), lines)

answer = xmas
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
