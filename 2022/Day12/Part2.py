with open("input.txt") as f:
    heightmap = [[ord(x) - 96 if ord(x) - 96 != -27 else 27 for x in list(i.strip())] for i in f]


def neighbors(row, col, visited):
    n = []
    for down, right in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        if 0 <= row + down < len(heightmap) and 0 <= col + right < len(heightmap[0]):
            if f'{row + down},{col + right}' not in visited:
                value = heightmap[row][col]
                if heightmap[row + down][col + right] in range(value - 100, value + 2):
                    visited.add(f'{row + down},{col + right}')
                    n.append([row + down, col + right])
    return n


def calculate(row, col):
    heightmap[row][col] = 1
    visited = set()
    visited.add(f'{row},{col}')
    edges = [[row, col]]
    steps = 0

    while True:
        steps += 1
        if not edges:
            return len(heightmap) * len(heightmap[0])
        for _ in list(edges):
            edge = edges.pop(0)
            for row, col in neighbors(edge[0], edge[1], visited):
                if heightmap[row][col] == 27:
                    return steps
                edges += [[row, col]]


startingpoints = []
lowest = len(heightmap) * len(heightmap[0])

for x, row in enumerate(heightmap):
    for y, col in enumerate(row):
        if heightmap[x][y] == 1 or heightmap[x][y] == -13:
            startingpoints.append([x, y])

for row, col in startingpoints:
    steps = calculate(row, col)
    if steps < lowest:
        lowest = steps

print(lowest)

