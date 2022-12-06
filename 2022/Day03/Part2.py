import os.path

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    rucksacks = [i.strip() for i in f]

sum = 0

for i in range(0, len(rucksacks), 3):
    isFlagged = []
    for c in rucksacks[i]:
        if c not in isFlagged and all(c in x for x in rucksacks[i+1:i+3]):
            isFlagged.append(c)
            sum += ord(c) - 96 if c.islower() else ord(c) - 38

print(sum)
