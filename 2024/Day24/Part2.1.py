from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    initial, inputops = [line for line in f.read().split('\n\n')]

initvalues = {g.split(':')[0]: int(g.split(':')[1]) == 1 for g in initial.split('\n')}
operations = {g.split()[4]: (g.split()[0], g.split()[1], g.split()[2]) for g in inputops.split('\n')}


def geteq(gate: str, ops: dict) -> str:
    if gate.startswith('y') or gate.startswith('x'):
        return gate
    A, op, B = ops[gate]
    A = geteq(A, ops)
    B = geteq(B, ops)

    return f'{min(A, B)} {op} {max(A, B)}'


def geteq2(gate: str, ops: dict) -> (str, list):
    if gate.startswith('y') or gate.startswith('x'):
        return gate, [gate]
    A, op, B = ops[gate]
    aa, _, bb = ops[gate]
    A, ga = geteq2(A, ops)
    B, gb = geteq2(B, ops)

    return f'{min(A, B)} {op} {max(A, B)}', [min(aa, bb), max(aa, bb)] + ga + gb



def getwrongs(ops: dict) -> list:
    wrongs = []
    cout = ''
    for i in range(46):
        A, op, B = ops[f"z{i:02}"]

        if f"x{i:02}" in A:
            pass

        if i == 0:
            cout = f'({A} AND {B})'
        else:
            cout = f'(({A} AND {B}) OR ({cout} AND ({A} XOR {B})))'

        pass
    return wrongs



def printzequations(ops: dict):
    length = 0
    for i in range(4, 5):
        eq = geteq(f"z{i:02}", ops)
        #print(eq)
        print(len(eq) - length)
        length = len(eq)
        for n in range(i):
            if f"x{n:02}" not in eq or f"y{n:02}" not in eq:
                pass

        pass



answer = 0
printzequations(operations)
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')

# wrong outputs z11
