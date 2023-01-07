import itertools as it

with open("input.txt") as f:
    lines = [line for line in f.read().split('\n')]

number = 0

for line in lines:
    if (
            any(p[0] == p[1] and i[1] - i[0] > 1 for p, i in zip(it.combinations(it.pairwise(line), 2), it.combinations(range(len(line) - 1), 2))) and
            any(line[i] == line[i-2] for i in range(2, len(line)))
    ):
        number += 1

print(f'⭐⭐ Part 2: {number}')
