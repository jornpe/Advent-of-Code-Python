from pathlib import Path
import time
import re
import operator

start_time = time.time()
operations = {'<': operator.lt, '>': operator.gt}
valueindex = {'x': 0, 'm': 1, 'a': 2, 's': 3}

with open(Path(__file__).with_name('input.txt')) as f:
    input = f.read().split('\n\n')

completed = []
workflows = {}
parts = [('in', *map(int, re.findall(r'(\d+)', part))) for part in input[1].splitlines()]

for workflow in input[0].splitlines():
    parsed = re.findall(r'([a-zA-Z]+)(<|>)?(\d+)?:?([a-zA-Z]+)?', workflow)
    id = parsed[0][0]
    ratings = [(w, o, v, d) for w, o, v, d in parsed[1::]]
    workflows[id] = ratings

while parts:
    flow, *values = parts.pop(0)
    if flow in 'AR':
        completed.append((flow, *values))
        continue

    wf = workflows[flow]

    for id, op, value, dest in wf:
        if op == '':
            parts.append((id, *values))
            break
        if operations[op](values[valueindex[id]], int(value)):
            parts.append((dest, *values))
            break

answer = sum([x + m + a + s for id, x, m, a, s in completed if id == 'A'])
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
