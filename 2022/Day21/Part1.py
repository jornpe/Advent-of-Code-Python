import operator

with open("input.txt") as f:
    monkeys = {m: c.strip() for m, c in [line.split(':') for line in f.read().split('\n')]}

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}


def get_root(monkey: str) -> int:
    cmd = monkeys[monkey]
    if cmd.isnumeric():
        return int(cmd)

    left, op, right = cmd.split()

    return ops[op](get_root(left), get_root(right))


print(get_root('root'))
