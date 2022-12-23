with open("../Day14/input.txt") as f:
    pairs = [i.split('\n') for i in f.read().split('\n\n')]


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


answer = sum(i for i, (left, right) in enumerate(pairs, 1) if check(eval(left), eval(right)) < 0)
print(answer)
