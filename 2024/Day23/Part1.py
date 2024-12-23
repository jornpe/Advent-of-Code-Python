from pathlib import Path
import time
from collections import defaultdict

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    connections = [line for line in f.read().split('\n')]

graph = defaultdict(list)

for con in connections:
    pc1, pc2 = con.split('-')
    graph[pc1].append(pc2)
    graph[pc2].append(pc1)

groups = []
for key, edges1 in graph.items():
    if key.startswith('t'):
        for edge1 in edges1:
            for edge2 in graph[edge1]:
                if edge2 != key and edge2 in graph[key]:
                    groups.append((key, edge1, edge2))

answer = len(set(tuple(sorted(t)) for t in groups))
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
