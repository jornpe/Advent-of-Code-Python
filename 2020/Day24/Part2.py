from collections import defaultdict
from pathlib import Path
import time
from pprint import pprint
import re

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

blacks = set()

for line in lines:
    row, col = 0, 0
    for d in re.findall(r'(e|se|sw|w|nw|ne)', line):
        match d:
            case 'e': col += 1
            case 'w': col -= 1
            case 'se':
                if row % 2 == 0:
                    col += 1
                row += 1
            case 'sw':
                if row % 2 == 1:
                    col -= 1
                row += 1
            case 'ne':
                if row % 2 == 0:
                    col += 1
                row -= 1
            case 'nw':
                if row % 2 == 1:
                    col -= 1
                row -= 1
    if (row, col) in blacks:
        blacks.remove((row, col))
    else:
        blacks.add((row, col))


def get_neigbours(r: int, c: int, grid: set) -> int:
    n = [(r, c - 1), (r, c + 1)]
    if r % 2 == 0:
        n.extend([(r - 1, c), (r - 1, c + 1), (r + 1, c), (r + 1, c + 1)])
    else:
        n.extend([(r - 1, c - 1), (r - 1, c), (r + 1, c - 1), (r + 1, c)])
    return sum(1 for p in n if p in grid)


for idx in range(100):
    updated = set()
    min_r = min(r for (r, _) in blacks) - 1
    max_r = max(r for (r, _) in blacks) + 2
    min_c = min(c for (_, c) in blacks) - 1
    max_c = max(c for (_, c) in blacks) + 2

    for row in range(min_r, max_r):
        for col in range(min_c, max_c):
            nb = get_neigbours(row, col, blacks)
            if nb == 2:
                updated.add((row, col))
            elif (row, col) in blacks and nb == 1:
                updated.add((row, col))

    blacks = updated

answer = len(blacks)
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
