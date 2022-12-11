with open("input.txt") as f:
    instructions = [i.strip() for i in f]

cycle = 0
register = 1
lookup = [20, 60, 100, 140, 180, 220]
total = 0

for ins in instructions:
    match ins:
        case 'noop':
            cycle += 1
            if cycle >= lookup[0]:
                total += lookup.pop(0) * register
        case _:
            _, value = ins.split()
            if cycle + 2 >= lookup[0]:
                total += lookup.pop(0) * register
            cycle += 2
            register += int(value)

    if len(lookup) == 0:
        break

print(total)
