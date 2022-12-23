import re
with open("input.txt") as f:
    lines = [i for i in f.read().split('\n')]

valves = {}

for line in lines:
    p1, p2 = line.split(';')
    valves[p1.split()[1]] = {'rate': int(p1.split('=')[1]), 'connections': re.split(', | ', p2)[5:], 'paths': {}}


def paths(source: str):
    paths = {}
    edges = list(valves[source]['connections'])
    steps = 0
    while edges:
        steps += 1
        for _ in list(edges):
            edge = edges.pop(0)
            if edge not in paths:
                paths[edge] = steps
                for v in valves[edge]['connections']:
                    if v not in edges and v != source:
                        edges.append(v)
    return paths


def travel(source: str):
    highest = 0
    travels = [(source, 0, 0, [source])]  # current, steps, pressure, path

    while travels:
        for _ in list(travels):
            t = travels.pop(0)
            edges = [p for p in valves[t[0]]['paths'] if valves[p]['rate'] != 0 and p not in t[3] and valves[t[0]]['paths'][p] < 30 - t[1]]
            if not edges or t[1] >= 30:
                if t[2] > highest:
                    highest = t[2]
                break
            for edge in edges:
                s = valves[t[0]]['paths'][edge] + 1
                travels.append((edge, t[1] + s, t[2] + valves[edge]['rate'] * (30 - t[1] - s), list(t[3]) + [edge]))
    return highest


for v in valves:
    valves[v]['paths'] = paths(v)

answer = travel('AA')
print(answer)
