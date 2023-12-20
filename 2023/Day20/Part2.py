import math
from pathlib import Path
import time
from collections import deque

start_time = time.time()

with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

modules = {}
queue = deque()
conjunction = {'vt': 0, 'sk': 0, 'xc': 0, 'kk': 0}

for line in lines:
    module, recievers = line.split(' -> ')
    if module == 'broadcaster':
        modules[module] = ('broadcaster', *recievers.split(', '))
    elif module[0] == '%':
        modules[module[1::]] = ['%', False, *recievers.split(', ')]
    elif module[0] == '&':
        modules[module[1::]] = ['&', {}, *recievers.split(', ')]

for m in modules.items():
    key, (mt, state, *_) = m
    if mt == '&':
        for mm in modules.items():
            key2, (mt2, state2, *recievers2) = mm
            if key in recievers2:
                state[key2] = False


def update_state(cycle):
    m, *recievers = modules['broadcaster']
    for reciever in recievers:
        queue.append((reciever, m, False))

    while queue:
        mod, source, puls = queue.popleft()
        if mod not in modules:
            continue
        mt, state, *dests = modules[mod]

        if mt == '%' and not puls:
            state = not state
            pulse = state
            for d in dests:
                queue.append((d, mod, pulse))
            modules[mod][1] = state

        if mt == '&':
            state[source] = puls
            allhigh = not all(p for p in state.values())
            for d in dests:
                queue.append((d, mod, allhigh))
                if allhigh and mod in conjunction and conjunction[mod] == 0:
                    conjunction[mod] = cycle
            modules[mod][1] = state


cycle = 0
while not all(c != 0 for c in conjunction.values()):
    cycle += 1
    update_state(cycle)


answer = math.lcm(*conjunction.values())
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
