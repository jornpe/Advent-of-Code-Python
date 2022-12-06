with open("input.txt") as f:
    lines = [i.strip() for i in f]

width = len(lines[0])
trees = []
slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

for slope in slopes:
    tree = 0
    current = 0
    for i, line in enumerate(lines):
        if i % slope[1] != 0:
            continue
        if current >= width:
            current -= width
        if line[current] == '#':
            tree += 1
        current += slope[0]
    trees.append(tree)

answer = 1
for t in trees:
    answer *= t
print(answer)