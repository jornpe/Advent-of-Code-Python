with open("input.txt") as f:
    input = f.read()
    print(f'⭐ Part 1: {input.count("(") - input.count(")")}')

    floor = 0
    for i, c in enumerate(input, 1):
        floor = floor + 1 if c == '(' else floor - 1
        if floor == -1:
            print(f'⭐ Part 2: {i}')
            break
