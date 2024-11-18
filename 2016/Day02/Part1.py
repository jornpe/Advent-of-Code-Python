from pathlib import Path
import time
from pprint import pprint

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

code = []
pos = (1,1)

directions = {
    'U': (0, -1),
    'R': (1, 0),
    'D': (0, 1),
    'L': (-1, 0)
}

for line in lines:
    for step in list(line):
        move = directions[step]
        pos = (min(max(pos[0] + move[0], 0), 2), min(max(pos[1] + move[1], 0), 2))
    code.append(pos[0] + 1 + (pos[1] * 3))


answer = int(''.join(map(str, code)))
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
