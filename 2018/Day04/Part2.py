from pathlib import Path
import time
from datetime import datetime
import re
from collections import Counter
from pprint import pprint

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    guardactions = [line for line in f.read().split('\n')]

actions = []

for ga in guardactions:
    dt = datetime.strptime(ga[1:17], '%Y-%m-%d %H:%M')
    action = ga[19::]
    if action.startswith('Guard'):
        actions.append((dt, 0, int(re.findall(r'\d+', action)[0])))
    if action.startswith('falls'):
        actions.append((dt, 1))
    if action.startswith('wakes'):
        actions.append((dt, 2))

actions.sort(key=lambda x: x[0])

guardtimes = {g[2]: [] for g in actions if g[1] == 0}
guardonduty = 0
for action in actions:
    match action[1]:
        case 0: guardonduty = action[2]
        case 1: sleeptimer: datetime = action[0]
        case 2:
            minutes = guardtimes[guardonduty]
            minutes.extend(list(range(sleeptimer.minute, action[0].minute)))
            guardtimes[guardonduty] = minutes

guard, value = max(guardtimes.items(), key=lambda g: max(Counter(g[1]).values(), default=0))
answer = guard * max(set(value), key=value.count)
print(f'⭐⭐ Part 2: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
