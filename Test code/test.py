# # from treelib import Node, Tree
# import itertools as it
import numpy as np
import itertools

test = {}

test[1] = {1:'a'}

pass

# #
# # print(str(101).zfill(4)[-3])
# # mode3, mode2, mode1 = f"{101 // 100:03d}"
# # print(f'{1234:04d}'[:-2][::-1])
#
# #
# # print(list(map(int, f'{1:05d}')))
#
# #
# # for n in it.permutations(range(5, 10), 5):
# #     print(n)

#
# min_y = max(max(x, y) / min(x, y), x) / min(max(x, y) / min(x, y), x)
# min_x = max(max(x, y) / min(x, y), y) / min(max(x, y) / min(x, y), y)
#
# if min_x.is_integer() and min_y.is_integer():
#     x = int(min_x)
#     y = int(min_y)
#
#
#
# def get_step(x: int, y: int) -> tuple:
#     if x == 0:
#         return x, int(y / abs(y))
#     if y == 0:
#         return int(x / abs(x)), y
#     for i in range(max(abs(x), abs(y)), 0, -1):
#         if (x / i).is_integer() and (y / i).is_integer():
#             return int(x / i), int(y / i)
#
#
# x = -2
# y = 0
#
# step = get_step(x, y)
#
# print(step)
#

# test = {(5, 1): 0, (0, 2): 0, (1, 0): 0, (0, 1): 0, (1, 2): 0, (6, 1): 1, (7, 0): 1, (5, 2): 0, (1, 1): 0, (6, 0): 1}
#
# max_x = max([pos[0] for pos in test.keys()])
# min_x = min([pos[0] for pos in test.keys()])
# max_y = max([pos[1] for pos in test.keys()])
# min_y = min([pos[1] for pos in test.keys()])
#
# print(max_x, min_x, max_y, min_y)
