from collections import defaultdict
from pathlib import Path
import time
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

answer = len(blacks)
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
