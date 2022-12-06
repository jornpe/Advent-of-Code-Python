import os.path
import re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    inputs = f.read()

crates, movement = inputs.split("\n\n")
crates = crates.split("\n")
stacks = []

for i in range(1, len(crates[0]) - 1, 4):
    stack = []
    for j, crate in enumerate(crates):
        if crate[i] != ' ' and not crate[i].isdigit():
            stack.insert(0, crates[j][i])
    stacks.append(stack)

print(stacks)

for move in movement.split('\n'):
    s, f, t = [int(x) for x in move.split() if x.isdigit()]
    for i in range(s):
        item = stacks[f-1].pop()
        stacks[t-1].append(item)

answer = ''.join([x[-1] for x in stacks])

print(answer)
