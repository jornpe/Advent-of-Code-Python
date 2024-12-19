from pathlib import Path
import time
from queue import PriorityQueue

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    fallingbytes = [tuple(map(int, line.split(','))) for line in f.read().split('\n')]

gridsize = 71


def isblocked(pos: tuple, visited: set) -> bool:
    queue = PriorityQueue()
    queue.put((0, pos))
    while queue.qsize() != 0:
        length, p = queue.get()
        if p in visited:
            continue
        if p[0] == gridsize - 1 and p[1] == gridsize - 1:
            return False
        for n in [(p[0] + x, p[1] + y) for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]]:
            if not 0 <= n[0] < gridsize or not 0 <= n[1] < gridsize:
                continue
            if n in visited:
                continue
            queue.put((length + 1, n))
        visited.add(p)
    return True


answer = 0
visited = set()
for byte in fallingbytes:
    visited.add(byte)
    blocked = isblocked((0, 0), set(visited))
    if blocked:
        answer = f'{byte[0]},{byte[1]}'
        break

print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
