import ast

with open("input.txt") as f:
    inputs = [i for i in f.read().split('\n')]

beacons = []
q1 = set()
q2 = set()
q3 = set()
q4 = set()


def parse_sensor(line: str):
    line = line.replace('Sensor at x=', '')\
               .replace(' y=', '')\
               .replace(': closest beacon is at x=', ',')\
               .replace(' y=', '')
    sx, sy, bx, by = ast.literal_eval(line)
    return (sx, sy), (bx, by)


def get_edges(s: tuple, b: tuple):
    l = abs(s[0] - b[0]) + abs(s[1] - b[1]) + 1
    for i in range(l, 0, -1):
        q1.add((s[0] + l - i, s[1] - i))
    for i in range(l, 0, -1):
        q2.add((s[0] + i, s[1] + l - i))
    for i in range(l, 0, -1):
        q3.add((s[0] - l + i, s[1] + i))
    for i in range(l, 0, -1):
        q4.add((s[0] - i, s[1] - l + i))


for input in inputs:
    s, b = parse_sensor(input)
    get_edges(s, b)

for c in q1:
    if c in q2 and c in q3 and c in q4:
        print((c[0] * 4000000) + c[1])
