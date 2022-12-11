import os.path
import numbers

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    inputs = [i.strip().replace('$ ', '') for i in f]

dirSizes = {}
currentDir = []
for input in inputs:
    if input.startswith('ls'):
        continue

    part1, part2 = input.split()
    if part1 == 'cd':
        if part2 == '/':
            currentDir.clear()
        elif part2 == '..':
            value = int(dirSizes.get(''.join(currentDir)))
            currentDir.pop()
            dirSizes[''.join(currentDir)] += value
        else:
            currentDir.append(part2)
            dirSizes[''.join(currentDir)] = 0
    elif part1.isnumeric():
        curDir = ''.join(currentDir)
        if curDir not in dirSizes:
            dirSizes[curDir] = int(part1)
        else:
            dirSizes[curDir] += int(part1)

for d in list(currentDir):
    fromDir = currentDir.pop()
    dirSizes[''.join(currentDir)] += dirSizes.get(''.join(currentDir) + fromDir)


print(dirSizes)

toDelete = 30000000 - (70000000 - int(dirSizes.get('')))

smallest = 70000000
for value in dirSizes.values():
    if toDelete < value < smallest:
        smallest = value

print(smallest)
