import math

with open("input.txt") as f:
    numbers = [line for line in f.read().split('\n')]


def calculate_remaining_fuel(fuel: int) -> int:
    f = math.floor(int(fuel) / 3) - 2
    if f < 1:
        return 0
    return f + calculate_remaining_fuel(f)


def calculate_fuel(numbers: list) -> int:
    answer = 0
    for n in numbers:
        fuel = math.floor(int(n) / 3) - 2
        answer += calculate_remaining_fuel(fuel) + fuel
    return answer


print(f'⭐⭐ Part 2: {calculate_fuel(numbers)}')
