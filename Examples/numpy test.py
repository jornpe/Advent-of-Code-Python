from pprint import pprint

import numpy as np

array = []
index = 0

for _ in range(5):
    line = []
    for _ in range(10):
        line.append(index)
        index += 1
    array.append(line)


y = np.array(array)

# rotating
pprint(y)
y = np.rot90(y)
pprint(y)
# K=2 means the rotation happends 2 times, so 180 rotation
y = np.rot90(y, 2)
pprint(y)
y = np.rot90(y)


# iterate over a numpy array
ints = []
for line in y:
    for i in line:
        ints.append(i)
print(ints)

