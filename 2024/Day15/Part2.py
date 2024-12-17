from pathlib import Path
import time
from sympy import Point2D

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    initialmap, movement = [line for line in f.read().split('\n\n')]

warehouse = []
pos = Point2D()
directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

for row, line in enumerate(initialmap.split('\n')):
    wline = []
    for col, c in enumerate(line):
        if c == '@':
            pos = Point2D(row, col * 2)
            wline.append('.')
            wline.append('.')
        elif c == '.' or c == '#':
            wline.append(c)
            wline.append(c)
        elif c == 'O':
            wline.append('[')
            wline.append(']')
    warehouse.append(wline)


def moveupordown(op: Point2D, move: str) -> bool:
    queue = [op]
    tomove = []
    dotts = []
    while queue:
        p = queue.pop()
        c = warehouse[p.x][p.y]
        other = ()
        otherc = ''

        if c == '.':
            continue
        if c == '#':
            return False
        if c == '[':
            other = directions['>']
            otherc = ']'
        if c == ']':
            other = directions['<']
            otherc = '['
        tomove.append((c, p + directions[move]))
        tomove.append((otherc, p + directions[move] + other))
        queue.append(p + directions[move])
        queue.append(p + directions[move] + other)
        dotts.append(p)
        dotts.append(p + other)
        queue = list(set(queue))

    boxes = []
    for c, p in tomove:
        warehouse[p.x][p.y] = c
        boxes.append(p)
    for p in dotts:
        if p not in boxes:
            warehouse[p.x][p.y] = '.'
    return True


for move in movement.replace('\n', ''):
    npos: Point2D = pos + directions[move]
    nc = warehouse[npos.x][npos.y]
    if nc == '.':
        pos = npos

    elif move in ['<', '>']:
        while nc not in ['.', '#']:
            npos += directions[move]
            nc = warehouse[npos.x][npos.y]
            if nc == '.':
                pos += directions[move]
                warehouse[npos.x].pop(npos.y)
                warehouse[pos.x].insert(pos.y, '.')

    else:
        canmove = moveupordown(npos, move)
        if canmove:
            pos = npos

answer = sum(100 * row + col for row, line in enumerate(warehouse) for col, c in enumerate(line) if c == '[')
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')

