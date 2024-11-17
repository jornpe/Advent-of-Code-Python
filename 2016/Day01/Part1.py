from operator import indexOf
from pathlib import Path
import time
from pprint import pprint

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    steps = [(line.strip()[0], int(line.strip()[1:])) for line in f.read().split(',')]

x, y = 0, 0

for dir, move in steps:
    x, y = (-y, x) if dir == 'R' else (y, -x)
    x += int(move)

answer = abs(x) + abs(y)
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
