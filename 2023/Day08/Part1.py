from itertools import cycle
from pathlib import Path
import re
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n\n')]

directions = list([0 if d == 'L' else 1 for d in lines[0]])
instructions = {}

for line in lines[1].split('\n'):
    nodes = re.findall(r'\w+', line)
    instructions[nodes[0]] = (nodes[1], nodes[2])

steps = 0
position = 'AAA'

for direction in cycle(directions):
    steps += 1
    position = instructions[position][direction]
    if position == 'ZZZ':
        break


print(f'⭐ Part 1: {steps}, run time: {int((time.time() - start_time) * 1000)}ms')
