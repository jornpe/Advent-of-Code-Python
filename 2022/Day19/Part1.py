import re

# 0: ore, 1: clay, 2: obsidian, 3: geode
with open("input.txt") as f:
    inputs = [line for line in f.read().split('\n')]
    bps = []
    for input in inputs:
        bp = []
        maxvalue = [0, 0, 0]
        for i, cost in enumerate(input.split('.')):
            if not cost:
                continue
            cost_of_one = [i]
            for amount, resource in re.findall(r'(\d+) (\w+)', cost):
                amount = int(amount)
                resource = ['ore', 'clay', 'obsidian', 'geode'].index(resource)
                cost_of_one.append((resource, amount))
                maxvalue[resource] = max(maxvalue[resource], amount)
            bp.append(cost_of_one)
        bps.append(bp)
        bp.append(maxvalue)


# 0: ore, 1: clay, 2: obsidian, 3: geode
def calculate_best(amount_of_each: list, robots: list, minutes_left: int, blueprint: list, max_of_each: list, cache: dict) -> int:
    max_geo = 0
    if minutes_left == 1:
        return amount_of_each[3] + robots[3]

    key = (minutes_left, *amount_of_each, *robots)
    if key in cache:
        return cache[key]

    # Don't create another, just wait one minute. Stop doing this if you have max of all resources except for geo
    if not all(amount_of_each[i] >= max_of_each[i] for i in range(len(max_of_each))):
        new_amounts2 = list(amount_of_each)
        for idx, robot in enumerate(robots):
            new_amounts2[idx] += robot
        max_geo = max(calculate_best(new_amounts2, list(robots), minutes_left - 1, blueprint, max_of_each, cache), max_geo)

    for recipe in blueprint:
        if recipe[0] != 3 and robots[recipe[0]] >= max_of_each[recipe[0]]:
            continue
        if all(amount_of_each[r] >= a for r, a in recipe[1:]):
            new_robots = list(robots)
            new_amounts = list(amount_of_each)
            new_robots[recipe[0]] += 1
            for type, cost in recipe[1:]:
                new_amounts[type] -= cost
            for idx, robot in enumerate(robots):
                new_amounts[idx] += robot
            geo = calculate_best(new_amounts, new_robots, minutes_left - 1, blueprint, max_of_each, cache)
            max_geo = max(geo, max_geo)

    cache[key] = max_geo
    return max_geo


answer = 0
for bid, bp in enumerate(bps):
    ql = calculate_best([0, 0, 0, 0], [1, 0, 0, 0], 24, bp[:-1], bp[-1], {})
    answer += (1 + bid) * ql
print(answer)
