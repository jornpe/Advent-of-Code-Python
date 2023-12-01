with open("input.txt") as f:
    map = {(x, y) for y, line in enumerate(f.read().split('\n')) for x, c in enumerate(list(line)) if c == '#'}


def get_step(x: int, y: int) -> tuple:
    if x == 0:
        return x, int(y / abs(y))
    if y == 0:
        return int(x / abs(x)), y
    for i in range(max(abs(x), abs(y)), 0, -1):
        if (x / i).is_integer() and (y / i).is_integer():
            return int(x / i), int(y / i)


def get_visible_astroids(station: tuple, map: set) -> set:
    max_x = max(x for x, y in map)
    max_y = max(y for x, y in map)
    in_sight = set(map)
    in_sight.remove(station)

    for ast in list(in_sight):
        step = get_step(ast[0] - station[0], ast[1] - station[1])
        pos = ast
        while 0 <= pos[0] <= max_x and 0 <= pos[1] <= max_y:
            pos = pos[0] + step[0], pos[1] + step[1]
            if pos in in_sight:
                in_sight.remove(pos)
    return in_sight


def get_best_astroid(map: set) -> tuple:
    best_astroid = (0, 0), 0
    for station in map:
        in_sight = get_visible_astroids(station, map)
        if len(in_sight) > best_astroid[1]:
            best_astroid = (station, len(in_sight))
    return best_astroid


def get_200_vaporized(station: tuple, map: set) -> int:
    target = 200
    vaporized = 0
    sx, sy = station
    while True:
        new_map = set(map)
        visible = get_visible_astroids(station, new_map)
        for dirs in range(8):
            match dirs:
                case 0:
                    ast = next(([(x, y)] for x, y in visible if x == sx and y < sy), [])
                    if vaporized + 1 == target and ast:
                        return next(100 * x + y for x, y in visible if y == sy)
                    vaporized += len(ast)

                case 1:
                    q = {(x, y): (sy - y)/(x - sx) for x, y in visible if (x - sx) > 0 and (sy - y) > 0}
                    if vaporized + len(q) < target:
                        vaporized += len(q)
                        continue
                    astX, astY = next(key for key, value in q.items() if value == sorted(q.values(), reverse=True)[target - vaporized - 1])
                    return 100 * astX + astY

                case 2:
                    ast = next(([(x, y)] for x, y in visible if y == sy and x > sx), [])
                    if vaporized + 1 == target and ast:
                        return next(100 * x + y for x, y in visible if y == sy)
                    vaporized += len(ast)

                case 3:
                    q = {(x, y): (y - sy) / (x - sx) for x, y in visible if (x - sx) > 0 and (y - sy) > 0}
                    if vaporized + len(q) < target:
                        vaporized += len(q)
                        continue
                    astX, astY = next(key for key, value in q.items() if value == sorted(q.values())[target - vaporized - 1])
                    return 100 * astX + astY

                case 4:
                    ast = next(([(x, y)] for x, y in visible if x == sx and y > sy), [])
                    if vaporized + 1 == target and ast:
                        return next(100 * x + y for x, y in visible if y == sy)
                    vaporized += len(ast)

                case 5:
                    q = {(x, y): (y - sy) / (sx - x) for x, y in visible if (sx - x) > 0 and (y - sy) > 0}
                    if vaporized + len(q) < target:
                        vaporized += len(q)
                        continue
                    astX, astY = next(key for key, value in q.items() if value == sorted(q.values(), reverse=True)[target - vaporized - 1])
                    return 100 * astX + astY

                case 6:
                    ast = next(([(x, y)] for x, y in visible if y == sy and x < sx), [])
                    if vaporized + 1 == target and ast:
                        return next(100 * x + y for x, y in visible if y == sy)
                    vaporized += len(ast)

                case 7:
                    q = {(x, y): (sy - y) / (sx - x) for x, y in visible if (sx - x) > 0 and (sy - y) > 0}
                    if vaporized + len(q) < target:
                        vaporized += len(q)
                        continue
                    test = sorted(q.values())
                    astX, astY = next(key for key, value in q.items() if value == sorted(q.values())[target - vaporized - 1])
                    return 100 * astX + astY


answer1 = get_best_astroid(map)
answer2 = get_200_vaporized(answer1[0], map)

print(f'⭐ Part 1: Asteroid {answer1[0]} can see {answer1[1]} asteroids')
print(f'⭐ Part 2: Asteroid {answer2} is the 200th asteroid to be vaporized')