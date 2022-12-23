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
    travels = [(source, source, 0, 0, 0, [source])]  # human, elefant, humanSteps, elefantSteps, pressure, path

    while travels:
        for _ in list(travels):
            t = travels.pop(0)
            hedges = [p for p in valves[t[0]]['paths'] if valves[p]['rate'] != 0 and p not in t[5] and valves[t[0]]['paths'][p] < 26 - t[2]]
            eedges = [p for p in valves[t[1]]['paths'] if valves[p]['rate'] != 0 and p not in t[5] and valves[t[1]]['paths'][p] < 26 - t[3]]
            if not hedges and not eedges or t[2] >= 26 and t[3] >= 26:
                if t[4] > highest:
                    highest = t[4]
                    print(highest)
                break
            for hu_edge in hedges:
                for el_edge in eedges:
                    if hu_edge == el_edge:
                        continue

                    if t[2] < 26 and t[3] < 26:
                        s1 = valves[t[0]]['paths'][hu_edge] + 1
                        s2 = valves[t[1]]['paths'][el_edge] + 1
                        pressure = t[4] + valves[hu_edge]['rate'] * (26 - t[2] - s1) + valves[el_edge]['rate'] * (26 - t[3] - s2)
                        travels.append((hu_edge, el_edge, t[2] + s1, t[3] + s2, pressure, list(t[5]) + [hu_edge, el_edge]))

                    elif t[2] >= 26 and t[3] < 26:
                        s = valves[t[1]]['paths'][el_edge] + 1
                        travels.append((t[0],  el_edge, t[2], t[3] + s, t[4] + valves[el_edge]['rate'] * (30 - t[3] - s), list(t[5]) + [el_edge]))

                if t[2] < 26 and t[3] >= 26:
                    s = valves[t[0]]['paths'][hu_edge] + 1
                    travels.append((hu_edge, t[1], t[2] + s, t[3], t[4] + valves[hu_edge]['rate'] * (30 - t[2] - s), list(t[5]) + [hu_edge]))

    return highest


for v in valves:
    valves[v]['paths'] = paths(v)

answer = travel('AA')
print(answer)
