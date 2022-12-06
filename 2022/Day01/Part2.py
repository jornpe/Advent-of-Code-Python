from itertools import groupby

with open("input.txt") as f:
    lines = [i.strip() for i in f]

elfs = [" ".join(list(g)) for k, g in groupby(lines, key=bool) if k]

calories = []

for elf in elfs:
    calories.append(sum([int(x) for x in elf.split()]))
    
calories.sort(reverse=True)

print(sum(calories[0:3]))