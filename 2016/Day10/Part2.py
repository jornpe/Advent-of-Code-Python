import math
import re
from pathlib import Path
import time
from collections import defaultdict

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    instructions = [line for line in f.read().split('\n')]

outputs = defaultdict(lambda: [])
bots = defaultdict(lambda: [])
actions = {}

for init in [i for i in instructions if i.startswith('value')]:
    v, b = re.findall(r'\d+', init)
    if b in bots:
        bots[b] += [int(v)]
    else:
        bots[b] = [int(v)]

for act in [i for i in instructions if i.startswith('bot')]:
    _, bot, *action = re.findall(r'bot|output|\d+', act)
    actions[bot] = action
    pass

complete = False

while not complete:
    complete = True
    for bot, value in list(bots.items()):
        if len(value) == 2:
            complete = False
            bots[bot] = []
            a1, b1, a2, b2 = actions[bot]
            if a1 != 'output':
                bots[b1] += [min(value)]
            else:
                outputs[b1] += [min(value)]
            if a2 != 'output':
                bots[b2] += [max(value)]
            else:
                outputs[b1] += [min(value)]

answer = math.prod([v[0] for k, v in outputs.items() if k in ['0', '1', '2']])
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')