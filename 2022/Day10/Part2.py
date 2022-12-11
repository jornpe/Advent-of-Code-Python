with open("input.txt") as f:
    instructions = [i.strip() for i in f]

register = 0
pixels = ''

for ins in instructions:
    match ins:
        case 'noop':
            pixels += '#' if len(pixels) % 40 in range(register, register + 3) else '.'
        case _:
            _, value = ins.split()
            for i in range(2):
                pixels += '#' if len(pixels) % 40 in range(register, register + 3) else '.'
            register += int(value)

for row in range(6):
    line = ''
    for pos in range(row * 40, (row * 40) + 40):
        line += pixels[pos]
    print(line)

