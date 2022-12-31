from sympy import solve

with open("input.txt") as f:
    monkeys = {m: c.strip() for m, c in [line.split(':') for line in f.read().split('\n')]}


def get_equation(monkey: str) -> str:
    cmd = monkeys[monkey]
    if monkey == 'humn':
        return monkey
    if cmd.isnumeric():
        return cmd

    l, o, r = cmd.split()

    return f'({get_equation(l)} {o} {get_equation(r)})'


left, op, right = monkeys['root'].split()
match op:
    case '+':
        operator = '-'
    case '-':
        operator = '+'
    case '*':
        operator = '/'
    case _:
        operator = '*'

equation = f'{get_equation(left)} {operator} {get_equation(right)}'
answer = solve(equation)

print(answer[0])
