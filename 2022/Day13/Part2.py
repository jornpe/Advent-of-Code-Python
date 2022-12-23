with open("input.txt") as f:
    packets = [i for i in f.read().split('\n') if i]


def check(left, right) -> int:
    match left, right:
        case int(), int():
            return left - right
        case list(), list():
            for l, r in zip(left, right):
                if d := check(l, r):
                    return d
            return len(left) - len(right)
        case int(), list():
            return check([left], right)
        case list(), int():
            return check(left, [right])


deviders = [[[2]], [[6]]]
answer = 1

for i, devider in enumerate(deviders, 1):
    place = 0
    for packet in packets:
        if check(devider, eval(packet)) > 0:
            place += 1
    answer *= (place + i)

print(answer)
