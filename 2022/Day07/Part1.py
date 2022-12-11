import os.path
import numbers

with open(os.path.join(os.path.dirname(__file__), 'test.txt')) as f:
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

answer = sum(list([int(x) for x in dirSizes.values() if x <= 100000]))
print(answer)
