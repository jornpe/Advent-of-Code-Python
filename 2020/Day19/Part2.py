from pathlib import Path
import time
import textwrap

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


def get_allowed(rules, start):
    allowed = []
    queue = [('', [start])]
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
    return allowed


allowed42 = get_allowed(rules, 42)
allowed31 = get_allowed(rules, 31)
msg_sub_length = len(allowed42[0])
answer = 0

for msg in messages.split('\n'):
    if len(msg) % msg_sub_length == 0:
        ml = textwrap.wrap(msg, msg_sub_length)
        if ml[0] in allowed42 and ml[1] in allowed42:
            for i, p in enumerate(ml[2::], 2):
                if p in allowed42:
                    continue
                if p in allowed31:
                    if all(x in allowed31 for x in ml[i::]) and i > len(ml) / 2:
                        answer += 1
                    else:
                        break
                break

print(f'⭐⭐ Part 2: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
