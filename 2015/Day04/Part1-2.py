import hashlib

with open("input.txt") as f:
    input = f.read()


def get_solution(leading_string: str) -> int:
    solution_found = False
    number = 0
    while not solution_found:
        h = hashlib.md5(f'{input}{number}'.encode('utf-8')).hexdigest()
        if h.startswith(leading_string):
            return number
        number += 1


print(f'⭐ Part 1: {get_solution("00000")}')
print(f'⭐⭐ Part 2: {get_solution("000000")}')
