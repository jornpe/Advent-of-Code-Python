# Map function
from collections import Counter
from itertools import cycle

bools = [True, False, True, True]
print(list(map(lambda x: not x, bools)))

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers3 = [0.5, 0.5, 0.5]

result = map(lambda x, y, z: x + y + z, numbers1, numbers2, numbers3)
print(list(result))


# get coordinates around a value

def checkAround(row: int, col: int):
    return [[(row, col) for col in range(col - 1, col + 2)] for row in range(row - 1, row + 2)]


print(list(checkAround(2, 2)))

# all values in a list are equal

l1 = [1, 0, 0, 0]
l2 = [0, 0, 0, 0]

t1 = set(l2)

if set(l1) == 0:
    print("L1 are equal")
if set(l2) == {0}:
    print("L2 are equal")

# adding together tuples

pos = (3, 2)

pos2 = pos + (1, 0)
print(pos2)



