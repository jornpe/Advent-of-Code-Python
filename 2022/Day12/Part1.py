with open("input.txt") as f:
    heightmap = [[ord(x) - 96 if ord(x) - 96 != -27 else 27 for x in list(i.strip())] for i in f]

heightmap[20][0] = 1
visited = set()
visited.add(f'0,0')
edges = [[20, 0]]
steps = 0


def neighbors(row, col):
    n = []
    for down, right in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        if 0 <= row + down < len(heightmap) and 0 <= col + right < len(heightmap[0]):
            if f'{row + down},{col + right}' not in visited:
                value = heightmap[row][col]
                if heightmap[row + down][col + right] in range(value - 100, value + 2):
                    visited.add(f'{row + down},{col + right}')
                    n.append([row + down, col + right])
    return n


while True:
    steps += 1
    for _ in list(edges):
        edge = edges.pop(0)
        for row, col in neighbors(edge[0], edge[1]):
            if heightmap[row][col] == 27:
                print(steps)
                exit()
            edges += [[row, col]]