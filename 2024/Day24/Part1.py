from pathlib import Path
import time
from itertools import combinations, permutations

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    initial, inputops = [line for line in f.read().split('\n\n')]

gates = {g.split(':')[0]: int(g.split(':')[1]) == 1 for g in initial.split('\n')}
operations = {g.split()[4]: (g.split()[0], g.split()[1], g.split()[2]) for g in inputops.split('\n')}


def getboolean(gate: str, gates: dict, ops: dict) -> bool:
    if gate in gates:
        return gates[gate]

    g1, op, g2 = ops[gate]
    g1 = getboolean(g1, gates, ops)
    g2 = getboolean(g2, gates, ops)
    r = g1 and g2 if op == 'AND' else g1 or g2 if op == 'OR' else g1 ^ g2
    gates[gate] = r
    return r



result = []
for g in operations.keys():
    if g.startswith('z'):
        result.append((g, getboolean(g, gates, operations)))

answer = int("".join(str(int(b)) for k, b in reversed(sorted(result))), 2)
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
