import math
from pathlib import Path
import time
import networkx as nx
import re
import matplotlib.pyplot as plt

# TODO: Solve this is a general maner, this is a solution only fitting my input

start_time = time.time()
with open(Path(__file__).with_name('test.txt')) as f:
    lines = [line for line in f.read().split('\n')]

G = nx.Graph()

for line in lines:
    node, *connections = re.findall(r'\w+', line)
    for c in connections:
        G.add_edge(node, c)

# test input
# G.remove_edge('hfx', 'pzl')
# G.remove_edge('bvb', 'cmg')
# G.remove_edge('nvd', 'jqt')

# real input
# G.remove_edge('plt', 'mgb')
# G.remove_edge('dbt', 'tjd')
# G.remove_edge('jxm', 'qns')

answer = math.prod(map(len, (list(nx.connected_components(G)))))

print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')


nx.draw(G, with_labels=True)
plt.show()
