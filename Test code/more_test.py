# Map function
from collections import Counter
from itertools import cycle
from shapely import Polygon

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

test = [3, 4]
print(test[-3::])

from queue import PriorityQueue
pq = PriorityQueue()

pq.put((1, 'test', '1'))
pq.put((2, 'test', '2'))
pq.put((2, 'test', '2'))
pq.put((4, 'test', '3'))
pq.put((3, 'test', '4'))

print(pq.get())
print(pq.get())
print(pq.qsize())

print('Shaply')
coords = ((0, 0), (0, 2), (2, 2), (2, 0))
polygon = Polygon(coords)
print(polygon.area)


print('a'.upper())