from pathlib import Path
import time
from collections import deque

start_time = time.time()

with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

modules = {}
queue = deque()
pulses = []

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


def update_state():
    pulses.append(False)
    m, *recievers = modules['broadcaster']
    for reciever in recievers:
        queue.append((reciever, m, False))
        pulses.append(False)

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
                pulses.append(pulse)
            modules[mod][1] = state

        if mt == '&':
            state[source] = puls
            allhigh = not all(p for p in state.values())
            for d in dests:
                queue.append((d, mod, allhigh))
                pulses.append(allhigh)
            modules[mod][1] = state


for _ in range(1000):
    update_state()

highs = sum(1 for p in pulses if p)
lows = sum(1 for p in pulses if not p)

answer = highs * lows
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
