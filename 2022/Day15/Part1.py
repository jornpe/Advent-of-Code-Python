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
    beacons.append(beacon)
    get_positions(sensor, beacon)

for b in beacons:
    if b in area:
        area.remove(b)

answer = len(area)
print(answer)
