with open("input.txt") as f:
    input = [line for line in f.read().split('\n')]
    right = set((row, col) for row, line in enumerate(input) for col, char in enumerate(list(line)) if char == '>')
    left = set((row, col) for row, line in enumerate(input) for col, char in enumerate(list(line)) if char == '<')
    up = set((row, col) for row, line in enumerate(input) for col, char in enumerate(list(line)) if char == '^')
    down = set((row, col) for row, line in enumerate(input) for col, char in enumerate(list(line)) if char == 'v')

width = len(input[0])
height = len(input)
start = (0, input[0].index('.'))
end = (len(input) - 1, input[len(input) - 1].index('.'))
minutes = 0
positions = set()
positions.add(start)

while end not in positions:
    minutes += 1
    right_copy = list(right)
    right.clear()
    for b in right_copy:
        right.add((b[0], b[1] + 1)) if b[1] < width - 2 else right.add((b[0], 1))
    left_copy = list(left)
    left.clear()
    for b in left_copy:
        left.add((b[0], b[1] - 1)) if b[1] > 1 else left.add((b[0], width - 2))
    down_copy = list(down)
    down.clear()
    for b in down_copy:
        down.add((b[0] + 1, b[1])) if b[0] < height - 2 else down.add((1, b[1]))
    up_copy = list(up)
    up.clear()
    for b in up_copy:
        up.add((b[0] - 1, b[1])) if b[0] > 1 else up.add((height - 2, b[1]))

    for p1, p2 in list(positions):
        positions.remove((p1, p2))
        for m1, m2 in [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]:
            n_p = (p1 + m1, p2 + m2)
            if n_p == start or n_p == end or 0 < n_p[0] < height - 1 and 0 < n_p[1] < width - 1:
                if n_p not in left and n_p not in right and n_p not in down and n_p not in up:
                    if n_p not in positions:
                        positions.add(n_p)

print(minutes)
