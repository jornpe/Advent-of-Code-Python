from collections import Counter

with open("input.txt") as f:
    groups = [[list(c) for c in g.split('\n')] for g in f.read().split('\n\n')]

answer = 0

for group in groups:
    answer += sum(1 for v in Counter([x for y in group for x in y]).values() if v == len(group))

print(f'⭐⭐ Part 2: {answer}')
