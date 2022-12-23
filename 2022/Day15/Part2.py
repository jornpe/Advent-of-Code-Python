import ast

with open("input.txt") as f:
    inputs = [i for i in f.read().split('\n')]

beacons = []
area = set()


def parse_sensor(line: str):
    line = line.replace('Sensor at x=', '')\
               .replace(' y=', '')\
               .replace(': closest beacon is at x=', ',')\
               .replace(' y=', '')
    sx, sy, bx, by = ast.literal_eval(line)
    return (sx, sy), (bx, by)


def get_area(s: tuple, b: tuple):
    test = set()
    l = abs(s[0] - b[0]) + abs(s[1] - b[1])
    for q in [[1, 1], [-1, 1], [-1, -1], [1, -1]]:
        for i in range(0, min(l + 1, 4000001)):
            for j in range(0, min(l + 1 - i, 4000001)):
                current = (s[0] + (j * q[0]), s[1] + (i * q[1]))
                test.add(current)
                area.add((s[0] + (j * q[0]), s[1] + (i * q[1])))


def get_positions(s: tuple, b: tuple):
    line = 2000000
    l = abs(s[0] - b[0]) + abs(s[1] - b[1])
    offset = l - abs(s[1] - line)

    if s[1] < line < s[1] + l:
        for i in range(s[0] - offset, s[0] + offset + 1):
            area.add((i, line))

    elif s[1] > line > s[1] - l:
        for i in range(s[0] - offset, s[0] + offset + 1):
            area.add((i, line))


for input in inputs:
    sensor, beacon = parse_sensor(input)
    print(sensor, beacon)
    get_area(sensor, beacon)

for x in range(0, 4000001):
    for y in range(0, 4000001):
        area.add((x, y))
        if (x, y) not in area:
            print(x, y)

