from collections import deque
from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

garden = set()
pos = set()

for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == '.':
            garden.add((row, col))
        if char == 'S':
            pos.add((row, col))
            garden.add((row, col))


for count in range(64):
    npos = pos.copy()
    pos.clear()
    while npos:
        pr, pc = npos.pop()
        for sr, sc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr = pr + sr
            nc = pc + sc
            if (nr, nc) in garden:
                pos.add((nr, nc))


answer = len(pos)
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
