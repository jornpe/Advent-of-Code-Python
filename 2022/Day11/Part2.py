import operator

with open("input.txt") as f:
    input = f.read()

monkeys = input.split('\n\n')
cleanMonkeys = []  # [[79,98], '*', 19, 23, 2, 3]
commonModulo = 1

ops = {
    '+': operator.add,
    '*': operator.mul
}

for monkey in monkeys:
    lines = monkey.split('\n')
    cm = []
    cm.append(list(map(int, lines[1].strip().split(': ')[1].split(','))))
    op, by = lines[2].strip().split('old ')[1].split(' ')
    cm.append(op)
    cm.append('old' if by == 'old' else int(by))
    dev = int(lines[3].strip().split('by ')[1])
    commonModulo *= dev
    cm.append(dev)
    cm.append(int(lines[4].strip().split('monkey ')[1]))
    cm.append(int(lines[5].strip().split('monkey ')[1]))
    cm.append(0)

    cleanMonkeys.append(cm)
for i in range(10_000):
    for monkey in cleanMonkeys:
        while monkey[0]:
            item = monkey[0].pop(0)
            op = item if monkey[2] == 'old' else monkey[2]
            wl = int(ops[monkey[1]](item, op)) % commonModulo
            if wl % monkey[3] == 0:
                cleanMonkeys[monkey[4]][0].append(wl)
            else:
                cleanMonkeys[monkey[5]][0].append(wl)
            monkey[6] += 1

monkeybusiness = [x[6] for x in cleanMonkeys]
monkeybusiness.sort(reverse=True)

print(monkeybusiness[0] * monkeybusiness[1])
