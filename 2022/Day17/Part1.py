with open("input.txt") as f:
    jets = [c for c in f.read()]

tower = set()
hp = 0  # highest point


#                                          #
#                        #        ..#      #
#                       ###       ..#      #      ##
# Shapes: 0 = ####  1 = .#.   2 = ###  3 = #  4 = ##
#
def tetris(shape_type: int, hp: int):
    at_rest = False
    shape = []  # x, Y (col, row)
    match shape_type:
        case 0:
            shape = [(2, hp + 4), (3, hp + 4), (4, hp + 4), (5, hp + 4)]
        case 1:
            shape = [(3, hp + 6), (2, hp + 5), (3, hp + 5), (4, hp + 5), (3, hp + 4)]
        case 2:
            shape = [(4, hp + 6), (4, hp + 5), (2, hp + 4), (3, hp + 4), (4, hp + 4)]
        case 3:
            shape = [(2, hp + 7), (2, hp + 6), (2, hp + 5), (2, hp + 4)]
        case 4:
            shape = [(2, hp + 5), (3, hp + 5), (2, hp + 4), (3, hp + 4)]

    while not at_rest:
        jet = jets.pop(0)

        if jet == '>' and all(x != 6 and (x + 1, y) not in tower for x, y in shape):
            shape = [(x+1, y) for x, y in shape]
        elif jet == '<' and all(x != 0 and (x - 1, y) not in tower for x, y in shape):
            shape = [(x-1, y) for x, y in shape]
        jets.append(jet)

        if all(y != 1 and (x, y - 1) not in tower for x, y in shape):
            shape = [(x, y - 1) for x, y in shape]
        else:
            at_rest = True

    return shape


for i in range(2022):
    new_shape = tetris(i % 5, hp)
    for s in new_shape:
        tower.add(s)
    hp = max(y for x, y in new_shape + [(0, hp)])


print(hp)
