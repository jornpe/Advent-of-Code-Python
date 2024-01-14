from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    p1, messages = [line for line in f.read().split('\n\n')]

rules = {}
for rule in p1.splitlines():
    n, r = rule.split(':')
    if 'a' in r or 'b' in r:
        rules[int(n)] = r.replace('"', '').replace(' ', '')
    else:
        rules[int(n)] = [[int(lr) for lr in sr.split() if lr.isdigit()] for sr in r.split('|') ]

allowed = []
queue = [('', *rules[0])]
while queue:
    msg, subrules = queue.pop()
    if not subrules:
        allowed.append(msg)
        continue

    ru = subrules.pop(0)
    if isinstance(rules[ru], str):
        queue.append((msg + rules[ru], subrules))
    else:
        for nr in rules[ru]:
            queue.append((msg, nr + subrules))

answer = sum(1 for msg in messages.splitlines() if msg in allowed)

print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
