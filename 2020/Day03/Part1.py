with open("input.txt") as f:
    lines = [i.strip() for i in f]

width = len(lines[0])
current = 0
trees = 0

for line in lines:
    if current >= width:
        current -= width
    if line[current] == '#':
        trees += 1
    current += 3

print(trees)
