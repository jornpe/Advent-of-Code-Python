from pathlib import Path
import time
from queue import PriorityQueue

start_time = time.time()

with open(Path(__file__).with_name('input.txt')) as f:
    grid = [[int(x) for x in line] for line in f.read().splitlines()]


def get_shortestpath():
    edges = PriorityQueue()
    edges.put((0, 0, 0, 'R', 4))  # Needed to start at 4-10 so that it turns both directions in the start.
    coledge = len(grid[0]) - 1
    rowedge = len(grid) - 1
    visited = set()

    while True:

        edge = edges.get()
        value, row, col, dir, n = edge

        if (row, col, dir, n) in visited:
            continue

        visited.add((row, col, dir, n))

        if row == rowedge and col == coledge and n >= 4:
            return value

        minimum = 4
        maximum = 10
        newedges = []
        match dir:
            case 'U':
                if row > 0 and n < maximum: newedges.append((row - 1, col, dir, n + 1))
                if col < coledge and n >= minimum: newedges.append((row, col + 1, 'R', 1))
                if col > 0 and n >= minimum: newedges.append((row, col - 1, 'L', 1))
            case 'R':
                if col < coledge and n < maximum: newedges.append((row, col + 1, dir, n + 1))
                if row > 0 and n >= minimum: newedges.append((row - 1, col, 'U', 1))
                if row < rowedge and n >= minimum: newedges.append((row + 1, col, 'D', 1))
            case 'D':
                if row < rowedge and n < maximum: newedges.append((row + 1, col, dir, n + 1))
                if col < coledge and n >= minimum: newedges.append((row, col + 1, 'R', 1))
                if col > 0 and n >= minimum: newedges.append((row, col - 1, 'L', 1))
            case 'L':
                if col > 0 and n < maximum: newedges.append((row, col - 1, dir, n + 1))
                if row > 0 and n >= minimum: newedges.append((row - 1, col, 'U', 1))
                if row < rowedge and n >= minimum: newedges.append((row + 1, col, 'D', 1))

        for newedge in newedges:
            n_row, n_col, n_dir, n_n = newedge
            n_value = value + grid[n_row][n_col]
            edges.put((n_value, n_row, n_col, n_dir, n_n))


answer = get_shortestpath()
print(f'⭐⭐ Part 2: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
