import ast
import itertools

with open("input.txt") as f:
    lines = [[p.strip() for p in i.split('->')] for i in f.read().split('\n')]

points = set()


def get_points(p1, p2):
    for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
        for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
            points.add((x, y))


for line in lines:
    for point1, point2 in itertools.pairwise(line):
        get_points(ast.literal_eval(point1), ast.literal_eval(point2))


lowest = max([p[1] for p in points])
at_rest = 0
overflow = False

while not overflow:
    new_p = [500, 0]
    moving = True

    while moving:
        if new_p[1] > lowest:
            moving = False
            overflow = True

        if (new_p[0], new_p[1] + 1) not in points:
            new_p[1] += 1
            continue

        if (new_p[0] - 1, new_p[1] + 1) not in points:
            new_p[0] -= 1
            new_p[1] += 1
            continue

        if (new_p[0] + 1, new_p[1] + 1) not in points:
            new_p[0] += 1
            new_p[1] += 1
            continue

        points.add((new_p[0], new_p[1]))
        at_rest += 1
        moving = False

print(at_rest)
