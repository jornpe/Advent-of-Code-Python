import itertools as it

with open("input.txt") as f:
    start, end = map(int, f.read().split('-'))

passwords = 0

for i in range(start, end):
    if any(a == b for a, b in it.pairwise(str(i))) and all(int(a) <= int(b) for a, b in it.pairwise(str(i))):
        passwords += 1

print(f'⭐ Part 1: {passwords}')
