from itertools import groupby

with open("input.txt") as f:
    input = f.read()

groups = input.split('\n\n')
answer = 0

for group in groups:
    answer += len(set(group.replace('\n', '')))

print(f'⭐ Part 1: {answer}')
