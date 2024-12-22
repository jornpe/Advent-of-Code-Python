from pathlib import Path
import time
from queue import PriorityQueue
from itertools import pairwise

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    codes = [line for line in f.read().split('\n')]


def findpaths(sp: tuple, ep: tuple, allowed: set) -> list:
    paths = []
    queue = PriorityQueue()
    queue.put((1, [sp]))
    shortest = 100
    while queue.qsize() > 0:
        _, path = queue.get()
        p = path[-1]
        if len(path) > shortest:
            continue
        if p == ep:
            shortest = len(path)
            paths.append(path)

        for np in [(r + p[0], c + p[1]) for r, c in [(0, 1), (1, 0), (0, -1), (-1, 0)]]:
            if np in path or np not in allowed:
                continue
            queue.put((len(path) + 1, path + [np]))
    pass
    return paths



def getbetpath(pos: tuple, key: str, depth: int, keypad: dict, cache: dict, totaldepth: int) -> int:
    dkeyPos = {'A': (0, 2), '^': (0, 1), '<': (1, 0), 'v': (1, 1), '>': (1, 2)}

    paths = findpaths(pos, keypad[key], set(keypad.values()))
    best = []
    if (pos, key, depth) in cache:
        return cache[(pos, key, depth)]

    for path in paths:
        move = ''
        for (sr1, sc1), (sr2, sc2) in pairwise(path):
            move += '' if sr1 - sr2 == 0 else '^' if sr1 - sr2 > 0 else 'v'
            move += '' if sc1 - sc2 == 0 else '<' if sc1 - sc2 > 0 else '>'
        move += 'A'
        if depth != totaldepth:
            npos = (0, 2)
            nmove = 0
            for m in move:
                result = getbetpath(npos, m, depth + 1, dkeyPos, cache, totaldepth)
                cache[(npos, m, depth + 1)] = result
                nmove += result
                npos = dkeyPos[m]
            best.append(nmove)
        else:
            return len(move)
    return min(best)


nkeypad = {'A': (3, 2), '0': (3, 1), '1': (2, 0), '2': (2, 1), '3': (2, 2), '4': (1, 0),
           '5': (1, 1), '6': (1, 2), '7': (0, 0), '8': (0, 1), '9': (0, 2)}

answer1 = 0
for code in codes:
    best = 0
    pos = (3, 2)
    for c in code:
        best += getbetpath(pos, c, 1, nkeypad, {}, 3)
        pos = nkeypad[c]
    answer1 += best * int(code[:-1])

answer2 = 0
for code in codes:
    best = 0
    pos = (3, 2)
    for c in code:
        best += getbetpath(pos, c, 1, nkeypad, {}, 26)
        pos = nkeypad[c]
    answer2 += best * int(code[:-1])

print(f'⭐ Part 1: {answer1} ; run time: {int((time.time() - start_time) * 1000)}ms')
print(f'⭐⭐ Part 2: {answer2} ; run time: {int((time.time() - start_time) * 1000)}ms')
