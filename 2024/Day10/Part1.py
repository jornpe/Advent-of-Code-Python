from pathlib import Path
import time
from sympy import Point2D

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    grid = [list(map(int, line)) for line in f.read().split('\n')]


def testtrail(p: Point2D) -> int:
    paths = [p]
    result = set()
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while paths:
        p = paths.pop(0)
        ns = [p + d for d in dirs]
        for n in ns:
            if not 0 <= n.x <= len(grid) - 1 or not 0 <= n.y <= len(grid[0]) - 1:
                continue
            if grid[n.x][n.y] == 9 and grid[p.x][p.y] == 8:
                result.add(n)
            elif grid[n.x][n.y] == grid[p.x][p.y] + 1:
                paths.append(n)
    return len(result)


answer = sum(testtrail(Point2D(idxr, idxc)) for idxr, r in enumerate(grid) for idxc, c in enumerate(r) if c == 0)

print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
