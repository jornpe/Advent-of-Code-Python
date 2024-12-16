from collections import defaultdict
from pathlib import Path
import time
from sympy import Point2D

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    initialmap, movement = [line for line in f.read().split('\n\n')]

warehouse = defaultdict(list)
pos = Point2D()
directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}


for row, line in enumerate(initialmap.split('\n')):
    for col, c in enumerate(line):
        if c == '@':
            pos = Point2D(row, col)
            warehouse['.'].append((row, col))
        else:
            warehouse[c].append((row, col))


for move in movement.replace('\n', ''):
    npos: Point2D = pos + directions[move]
    if npos.args in warehouse['.']:
        pos = npos
    elif npos.args in warehouse['O']:
        boxes = warehouse['O'].copy()
        moved = []
        while npos.args in boxes:
            moved.append((npos + directions[move]).args)
            boxes.remove(npos.args)
            npos += directions[move]
        if npos.args in warehouse['.']:
            warehouse['.'].remove(npos.args)
            warehouse['O'] = boxes + moved
            pos = pos + directions[move]
            warehouse['.'].append(pos.args)


answer = sum(100 * r + c for r, c in warehouse['O'])
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')