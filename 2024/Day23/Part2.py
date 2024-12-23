from pathlib import Path
import time
from collections import defaultdict
from pprint import pprint

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    connections = [line for line in f.read().split('\n')]

graph = defaultdict(list)

for con in connections:
    pc1, pc2 = con.split('-')
    graph[pc1].append(pc2)
    graph[pc2].append(pc1)

parties = []
for key, edges in graph.items():
    party = [key]
    for edge in edges:
        if all(p in graph[edge] for p in party):
            party.append(edge)
    parties.append(party)

answer = ','.join(sorted(max(parties, key=len)))
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
