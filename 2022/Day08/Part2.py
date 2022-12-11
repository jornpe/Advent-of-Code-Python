with open("input.txt") as f:
    inputs = [list(map(int, list(i.strip()))) for i in f]

highest = 0


def scenic(n, row, col):
    up = down = right = left = 0

    for s in range(row - 1, -1, -1):
        if inputs[s][col] < n:
            up += 1
        else:
            up += 1
            break

    for s in range(row+1, len(inputs[0])):
        if inputs[s][col] < n:
            down += 1
        else:
            down += 1
            break

    for s in range(col - 1, -1, -1):
        if inputs[row][s] < n:
            right += 1
        else:
            right += 1
            break

    for s in range(col+1, len(inputs)):
        if inputs[row][s] < n:
            left += 1
        else:
            left += 1
            break

    return up * down * right * left


for row, i in enumerate(inputs):
    for col, c in enumerate(i):
        test = scenic(c, row, col)
        if test > highest:
            highest = test

print(highest)
