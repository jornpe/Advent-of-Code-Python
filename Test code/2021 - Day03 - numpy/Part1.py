# from https://dev.to/meseta/advent-of-code-2021-day-03-with-python-and-more-numpy-mj9

import numpy as np

lines = np.loadtxt("test.txt", "U")
bits = int(len(lines[0]))
data = lines.view('U1').astype(int).reshape(lines.shape[0], bits)
pow2 = 1 << np.arange(bits)[::-1]

ones = (data == 1).sum(axis=0)
zeros = (data == 0).sum(axis=0)
result = pow2.dot(ones > zeros) * pow2.dot(ones < zeros)
print("Part 1 result:", result)

a = b = data
for idx in range(bits):
    acol = a[:, idx]
    bcol = b[:, idx]
    a = a[acol == (acol.sum()*2 >= acol.size)] if len(a) > 1 else a
    b = b[bcol == (bcol.sum()*2 < bcol.size)] if len(b) > 1 else b
result = pow2.dot(a[0]) * pow2.dot(b[0])
print("Part 2 result:", result)
