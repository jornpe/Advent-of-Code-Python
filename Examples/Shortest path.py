from pathlib import Path
import time
from queue import PriorityQueue

#  https://adventofcode.com/2023/day/17
#  An example for shortes path using priority queue

start_time = time.time()

with open(Path(__file__).with_name('shortestpath.txt')) as f:
    grid = [[int(x) for x in line] for line in f.read().splitlines()]


# TODO: Change from using direction U, R, D, L to use direction row and col. That way the turning is easier.
# https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day17p1.py

def get_shortestpath():
    # initializes the queue and adds the start point.
    # important to add the value first as the priority queue sorts on values starting to the left.
    # value, row, col, direction, number of steps in direction
    edges = PriorityQueue()
    edges.put((0, 0, 0, 'R', 0))
    coledge = len(grid[0]) - 1
    rowedge = len(grid) - 1

    # add a visited dict
    visited = set()

    while True:
        # getting the item with lowest value to the left.
        edge = edges.get()
        value, row, col, dir, n = edge

        # check if the node is visited, if so continue to next. IF not add it to visited.
        if (row, col, dir, n) in visited:
            continue

        visited.add((row, col, dir, n))

        # Return first time any node hits the end.
        if row == rowedge and col == coledge:
            return value

        # get all the nodes we can visit from current node
        newedges = []
        match dir:
            case 'U':
                if row > 0 and n < 3: newedges.append((row - 1, col, dir, n + 1))
                if col < coledge: newedges.append((row, col + 1, 'R', 1))
                if col > 0: newedges.append((row, col - 1, 'L', 1))
            case 'R':
                if col < coledge and n < 3: newedges.append((row, col + 1, dir, n + 1))
                if row > 0: newedges.append((row - 1, col, 'U', 1))
                if row < rowedge: newedges.append((row + 1, col, 'D', 1))
            case 'D':
                if row < rowedge and n < 3: newedges.append((row + 1, col, dir, n + 1))
                if col < coledge: newedges.append((row, col + 1, 'R', 1))
                if col > 0: newedges.append((row, col - 1, 'L', 1))
            case 'L':
                if col > 0 and n < 3: newedges.append((row, col - 1, dir, n + 1))
                if row > 0: newedges.append((row - 1, col, 'U', 1))
                if row < rowedge: newedges.append((row + 1, col, 'D', 1))

        # add nodes to the queue with updated values
        for newedge in newedges:
            n_row, n_col, n_dir, n_n = newedge
            n_value = value + grid[n_row][n_col]
            edges.put((n_value, n_row, n_col, n_dir, n_n))


answer = get_shortestpath()
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
