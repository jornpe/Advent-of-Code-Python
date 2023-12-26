import math
from itertools import pairwise
from pathlib import Path
import time
from pprint import pprint

import networkx as nx
import re

from matplotlib import pyplot as plt

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

graph = nx.Graph()
edgeweights = {}

for line in lines:
    node, *connections = re.findall(r'\w+', line)
    for c in connections:
        graph.add_edge(node, c)


for node in graph.nodes:
    for nodetarget in graph.nodes:
        if node != nodetarget:
            for e1, e2 in pairwise(nx.shortest_path(graph, node, nodetarget)):
                if (e1, e2) in edgeweights:
                    edgeweights[(e1, e2)] += 1
                elif (e2, e1) in edgeweights:
                    edgeweights[(e2, e1)] += 1
                else:
                    edgeweights[(e1, e2)] = 1

for _ in range(3):
    e1, e2 = max(edgeweights, key=edgeweights.get)
    edgeweights.pop((e1, e2))
    if graph.has_edge(e1, e2):
        graph.remove_edge(e1, e2)
    if graph.has_edge(e2, e1):
        graph.remove_edge(e2, e1)


answer = math.prod(map(len, (list(nx.connected_components(graph)))))
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')

