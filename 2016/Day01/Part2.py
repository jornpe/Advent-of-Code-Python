from operator import indexOf
from pathlib import Path
import time
from pprint import pprint

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    steps = [line.strip() for line in f.read().split(',')]


def getAnswer():
    pos = [0, 0]
    fac = (1, 0)
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = set()
    for step in steps:
        dir, moves = 1 if step[0] == 'R' else -1, int(step[1:])
        fac = dirs[(dirs.index(fac) + dir) % 4]
        for move in range(moves):
            pos = (pos[0] + fac[0], pos[1] + fac[1])
            if pos in visited:
                return abs(pos[0]) + abs(pos[1])
            visited.add(pos)


answer = getAnswer()
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
