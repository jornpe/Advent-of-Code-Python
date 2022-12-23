from itertools import groupby

with open("test.txt") as f:
    lines = [i.strip() for i in f]

bags = []

for line in lines:
    btype, cap = line.split(' bags contain ')

    if cap.startswith('no'):
        bag = [btype, []]
        bags.append(bag)
        continue

    capacity = []
    for c in cap.split(','):
        c = c.replace('bags', '').replace('bag', '').strip()
        n, b = c.split(' ', 1)
        capacity.append({int(n), b})

    bags.append([btype, capacity])

print(bags)