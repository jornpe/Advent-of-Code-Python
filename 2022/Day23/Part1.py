map = {}

with open("input.txt") as f:
    input = [line for line in f.read().split('\n')]
    for r, l in enumerate(input):
        for c, char in enumerate(l):
            if char == '#':
                map[len(map)] = (r, c)

north = [[-1, -1], [-1, 0], [-1, 1]]
east = [[-1, 1], [0, 1], [1, 1]]
south = [[1, 1], [1, 0], [1, -1]]
west = [[1, -1], [0, -1], [-1, -1]]

number_elfs = len(map)
directions = ['N', 'S', 'W', 'E']


def move(elf: list, staging: dict, dirs: list) -> dict:

    for dir in dirs:
        if not any((elf[0] + row, elf[1] + col) in map.values() for row, col in north + east + south + west):
            return staging
        elif dir == 'N' and not any((elf[0] + row, elf[1] + col) in map.values() for row, col in north):
            staging[i] = (elf[0] - 1, elf[1])
            return staging
        elif dir == 'S' and not any((elf[0] + row, elf[1] + col) in map.values() for row, col in south):
            staging[i] = (elf[0] + 1, elf[1])
            return staging
        elif dir == 'W' and not any((elf[0] + row, elf[1] + col) in map.values() for row, col in west):
            staging[i] = (elf[0], elf[1] - 1)
            return staging
        elif dir == 'E' and not any((elf[0] + row, elf[1] + col) in map.values() for row, col in east):
            staging[i] = (elf[0], elf[1] + 1)
            return staging

    return staging


for idx in range(10):
    staging = {}
    for i in range(number_elfs):
        elf = map.get(i)
        staging = move(elf, staging, directions)

    directions = directions + [directions.pop(0)]

    values = list(staging.values())
    for key, value in list(staging.items()):
        if values.count(value) > 1:
            for k, v in list(staging.items()):
                if v == value:
                    del staging[k]

    for i, e in staging.items():
        map[i] = e

height = max(row for row, col in map.values()) - min(row for row, col in map.values()) + 1
width = max(col for row, col in map.values()) - min(col for row, col in map.values()) + 1

print((height * width) - len(map))
