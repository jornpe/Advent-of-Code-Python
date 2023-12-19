from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.animation as animation

with open(Path(__file__).with_name('input.txt')) as f:
    grid = [list(line) for line in f.read().splitlines()]



def beam_beams() -> tuple:
    visited = set()
    paths = [[(0, 0, 'R')]]
    completedpaths = []

    while paths:
        path = paths.pop(0)
        pos = path[-1]

        if pos in visited:
            completedpaths.append(path)
            continue

        row, col, dir = pos
        if col < 0 or col >= len(grid[0]) or row < 0 or row >= len(grid):
            continue

        nextpos = []

        match grid[row][col]:
            case '.' if dir in 'U': nextpos.append((row - 1, col, dir))
            case '.' if dir in 'R': nextpos.append((row, col + 1, dir))
            case '.' if dir in 'D': nextpos.append((row + 1, col, dir))
            case '.' if dir in 'L': nextpos.append((row, col - 1, dir))

            case '-' if dir in 'UD': nextpos.extend([(row, col + 1, 'R'), (row, col - 1, 'L')])
            case '-' if dir in 'R': nextpos.append((row, col + 1, dir))
            case '-' if dir in 'L': nextpos.append((row, col - 1, dir))

            case '|' if dir in 'U': nextpos.append((row - 1, col, dir))
            case '|' if dir in 'D': nextpos.append((row + 1, col, dir))
            case '|' if dir in 'RL': nextpos.extend([(row - 1, col, 'U'), (row + 1, col, 'D')])

            case '\\' if dir in 'U': nextpos.append((row, col - 1, 'L'))
            case '\\' if dir in 'R': nextpos.append((row + 1, col, 'D'))
            case '\\' if dir in 'D': nextpos.append((row, col + 1, 'R'))
            case '\\' if dir in 'L': nextpos.append((row - 1, col, 'U'))

            case '/' if dir in 'U': nextpos.append((row, col + 1, 'R'))
            case '/' if dir in 'R': nextpos.append((row - 1, col, 'U'))
            case '/' if dir in 'D': nextpos.append((row, col - 1, 'L'))
            case '/' if dir in 'L': nextpos.append((row + 1, col, 'D'))

        for n in nextpos:
            p = path.copy()
            p.append(n)
            paths.append(p)
        visited.add((row, col, dir))

    return completedpaths, len(set(((r, c) for r, c, _ in visited)))


paths, answer = beam_beams()
fig, ax = plt.subplots()


def animate(i):
    ax.clear()
    for path in paths:
        p = path[:(i * 5) + 1]
        cols = []
        rows = []
        for row, col, _ in p:
            cols.append(col)
            rows.append(row)
        ax.set_xlim([0, 120])
        ax.set_ylim([0, 120])
        ax.plot(rows, cols)


ani = animation.FuncAnimation(fig, animate, interval=10, frames=1000)
ani.save('animation2.gif', writer='PillowWriter', fps=30)
plt.close()
