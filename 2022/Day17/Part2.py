with open("input.txt") as f:
    jets = [c for c in f.read()]

tower = set()
hp = 0
tops = {}
max_rocks = 1000000000000
hp_added = 0
been_there_done_that = False
count_rocks = 0
jet_index = 0
top = [0, 0, 0, 0, 0, 0, 0]


#                                          #
#                        #        ..#      #
#                       ###       ..#      #      ##
# Shapes: 0 = ####  1 = .#.   2 = ###  3 = #  4 = ##
#
def tetris(shape_type: int, hp: int, jet_idx: int):
    at_rest = False
    shape = []
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
        jet = jets[jet_idx]
        if jet == '>' and all(x != 6 and (x + 1, y) not in tower for x, y in shape):
            shape = [(x+1, y) for x, y in shape]
        elif jet == '<' and all(x != 0 and (x - 1, y) not in tower for x, y in shape):
            shape = [(x-1, y) for x, y in shape]
        jet_idx = (jet_idx + 1) % len(jets)

        if all(y != 1 and (x, y - 1) not in tower for x, y in shape):
            shape = [(x, y - 1) for x, y in shape]
        else:
            at_rest = True

    return shape, jet_idx


while count_rocks < max_rocks:
    rock = count_rocks % 5
    new_shape, jet_index = tetris(count_rocks % 5, hp, jet_index)
    for s in new_shape:
        tower.add(s)
    hp = max(y for x, y in new_shape + [(0, hp)])

    for i in range(7):
        top[i] = max([y for x, y in new_shape if x == i and y > top[i]] + [top[i]])

    top_line = tuple(map(lambda x: x - min(top), top))

    if not been_there_done_that and (top_line, jet_index, rock) in tops:
        t = tops[(top_line, jet_index, rock)]
        been_there_done_that = True
        diff_height = hp - tops[(top_line, jet_index, rock)][0]
        diff_rocks = count_rocks - tops[(top_line, jet_index, rock)][1]

        multiplier = int((max_rocks - count_rocks) / diff_rocks)
        count_rocks += diff_rocks * multiplier
        hp_added += diff_height * multiplier
    else:
        tops[(top_line, jet_index, rock)] = (hp, count_rocks)
    count_rocks += 1

print(hp + hp_added)
