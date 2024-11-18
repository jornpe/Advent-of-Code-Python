from pathlib import Path
import time
from pprint import pprint

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

code = []
pos = (0,2)

directions = {
    'U': (0, -1),
    'R': (1, 0),
    'D': (0, 1),
    'L': (-1, 0)
}

key = {
    (2, 0): '1',
    (1, 1): '2',
    (2, 1): '3',
    (3, 1): '4',
    (0, 2): '5',
    (1, 2): '6',
    (2, 2): '7',
    (3, 2): '8',
    (4, 2): '9',
    (1, 3): 'A',
    (2, 3): 'B',
    (3, 3): 'C',
    (2, 4): 'D',
}

for line in lines:
    for step in list(line):
        move = directions[step]
        new_pos = (pos[0] + move[0], pos[1] + move[1])
        if new_pos in [(0,0),(1,0),(3,0),(4,0),(0,1),(4,1),(0,3),(4,3),(0,4),(1,4),(3,4),(4,4)] or not 0 <= new_pos[0] <= 4 or not 0 <= new_pos[1] <= 4:
            continue
        pos = new_pos
    code.append(key[pos])



answer = ''.join(code)
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
