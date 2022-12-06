import os.path

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    rucksacks = [i.strip() for i in f]

sum = 0

for rucksack in rucksacks:
    first = rucksack[:len(rucksack)//2]
    second = rucksack[len(rucksack)//2:]
    isFlagged = []

    for c in first:
        if c in second and c not in isFlagged:
            isFlagged.append(c)
            sum += ord(c) - 96 if c.islower() else ord(c) - 38

print(sum)