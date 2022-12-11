with open("input.txt") as f:
    inputs = [list(map(int, list(i.strip()))) for i in f]

visible = 0


def isvisible(n, row, col):
    check = []
    for s in range(0, row):
        check.append(inputs[s][col])
    if all(num < n for num in check):
        return True

    check.clear()
    for s in range(row+1, len(inputs[0])):
        check.append(inputs[s][col])
    if all(num < n for num in check):
        return True

    check.clear()
    for s in range(0, col):
        check.append(inputs[row][s])
    if all(num < n for num in check):
        return True

    check.clear()
    for s in range(col+1, len(inputs)):
        check.append(inputs[row][s])
    if all(num < n for num in check):
        return True
    return False


for row, i in enumerate(inputs):
    for col, c in enumerate(i):
        if col == 0 or col == len(i) - 1 or row == 0 or row == len(inputs) - 1:
            visible += 1
            continue
        if isvisible(c, row, col):
            visible += 1

print(visible)
