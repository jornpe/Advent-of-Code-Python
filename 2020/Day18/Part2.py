from pathlib import Path
import time
import re

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    equations = [line for line in f.read().split('\n')]


def solve(equation: str) -> str:
    if equation.isdigit():
        return equation

    if '(' in equation:
        subeq = re.findall(r'\(([0-9+*]+)\)', equation)
        for se in subeq:
            s_se = solve(se)
            equation = equation.replace(f'({se})', s_se, 1)
        return solve(equation)
    elif '+' in equation:
        additions = re.findall(r'([0-9+]+)', equation)
        for adds in additions:
            equation = equation.replace(adds, str(eval(adds)), 1)
        return solve(equation)
    else:
        start = re.findall(r'^(\d+[+*]\d+)', equation)[0]
        equation = equation.replace(start, str(eval(start)), 1)
        return solve(equation)


answer = []
for eq in equations:
    answer.append(int(solve(eq.replace(' ', ''))))

print(f'⭐⭐ Part 2: {sum(answer)}, run time: {int((time.time() - start_time) * 1000)}ms')
