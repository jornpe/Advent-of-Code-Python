import itertools

with open("input.txt") as f:
    lines = [line for line in f.read().split('\n')]

number = 0

for line in lines:
    if (
        len([i for i in list(line) if i in ['a', 'e', 'i', 'o', 'u']]) > 2 and
        any(right == left for right, left in itertools.pairwise(list(line))) and
        not any(test in line for test in ['ab', 'cd', 'pq', 'xy'])
    ):
        number += 1

print(f'⭐ Part 1: {number}')
