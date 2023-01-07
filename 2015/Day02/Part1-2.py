with open("input.txt") as f:
    boxes = [line for line in f.read().split('\n')]

total_paper = 0
total_ribbon = 0
for box in boxes:
    l, b, h = map(int, box.split('x'))
    total_paper += 2 * l * b + 2 * b * h + 2 * l * h + min(l * b, b * h, l * h)
    total_ribbon += 2 * l + 2 * b + 2 * h - 2 * max(l, b, h) + l * b * h

print(f'⭐ Part 1: {total_paper}')
print(f'⭐⭐ Part 2: {total_ribbon}')

