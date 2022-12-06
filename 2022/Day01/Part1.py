from itertools import groupby

with open("input.txt") as f:
    lines = [i.strip() for i in f]

elfs = [" ".join(list(g)) for k, g in groupby(lines, key=bool) if k]

highest = 0
for elf in elfs:
    calories = sum([int(x) for x in elf.split()])
    if calories > highest:
        highest = calories

print(highest)