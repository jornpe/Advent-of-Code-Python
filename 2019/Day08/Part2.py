with open("input.txt") as f:
    input = list(map(int, list(f.read())))

layers = [input[i:i+150] for i in range(0, len(input), 150)]

image = []

for pixel_layers in zip(*layers):
    pixel = [p for p in pixel_layers if p != 2][0]
    image.append(pixel)

for row in [image[i:i+25] for i in range(0, len(image), 25)]:
    line = ''
    for pixel in row:
        if pixel == 0:
            line += '.'
        else:
            line += '#'
    print(line)
