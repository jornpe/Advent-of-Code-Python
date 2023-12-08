import math
from itertools import cycle
from pathlib import Path
import re

with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n\n')]

directions = list([0 if d == 'L' else 1 for d in lines[0]])
instructions = {}

for line in lines[1].split('\n'):
    nodes = re.findall(r'\w+', line)
    instructions[nodes[0]] = (nodes[1], nodes[2])

steps = []
positions = [k for k in instructions.keys() if list(k)[2] == 'A']

for start in positions:
    step = 0
    position = start
    for direction in cycle(directions):
        step += 1
        position = instructions[position][direction]
        if position.endswith('Z'):
            steps.append(step)
            break


answer = math.lcm(*steps)
print(f'⭐⭐ Part 2: {answer}')
