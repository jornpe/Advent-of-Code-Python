from pathlib import Path
import time
from collections import defaultdict

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

garden = set()
pos = defaultdict(set)

for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == '.':
            garden.add((row, col))
        if char == 'S':
            garden.add((row, col))
            pos[(row, col)] = {(0,0)}


def expand(count: int, pos: defaultdict) -> defaultdict:
    for _ in range(count):
        npos = pos.copy()
        pos = defaultdict(set)
        while npos:
            (pr, pc), positions = npos.popitem()
            for sr, sc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nr = len(lines) - 1 if pr + sr < 0 else 0 if pr + sr >= len(lines) else pr + sr
                nc = len(lines[0]) - 1 if pc + sc < 0 else 0 if pc + sc >= len(lines[0]) else pc + sc

                if (nr, nc) in garden:
                    ngpos = positions.copy()
                    if not (0 <= pr + sr < len(lines) and 0 <= pc + sc < len(lines[0])):
                        ngr = 0 if 0 <= pr + sr < len(lines) else -1 if pr + sr < 0 else 1
                        ngc = 0 if 0 <= pc + sc < len(lines[0]) else -1 if pc + sc < 0 else 1

                        ngpos = set((gr + ngr, gc + ngc) for gr, gc in ngpos)
                    if (nr, nc) in pos:
                        pos[(nr, nc)] = ngpos.union(pos[(nr, nc)])
                    else:
                        pos[(nr, nc)] = ngpos
    return pos


# the idea here is that you need to interpolate the answer. This can be done because the input is a perfect square,
# and the S has no # to the right, left up or down.
# first get the value after hitting the edge, this is length / 2 = 65, then another 2 times to get compte length.
# then use the formula: a+n*(b-a+(n-1)*(c-b-b+a)//2)
# where a = 65 steps, b = 65 + 1 * 131 steps and c = 65 + 2 * 131.

steps = []
for s in [65, 131, 131]:
    pos = expand(s, pos)
    steps.append(sum(len(x) for x in pos.values()))

print(steps)

n = (26501365 - 65) / 131
f = lambda n,a,b,c: a+n*(b-a+(n-1)*(c-b-b+a)//2)
answer = f(n, *steps)

print(f'⭐⭐ Part 2: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
