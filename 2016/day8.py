import numpy as np

def parse(inp):
    out = []
    import re
    pat = re.compile(r'\d+')
    
    for line in inp.splitlines():
        x, y = map(int, pat.findall(line))
        if line.startswith('rect'):
            out.append(('rect', x, y))
        elif line.startswith('rotate column'):
            out.append(('column', x, y))
        elif line.startswith('rotate row'):
            out.append(('row', x, y))
    return out


def part1(inp):
    GRID = np.array([[0]*50 for _ in range(6)])

    for ins, a, b in inp:
        if ins == 'rect':
            GRID[:b, :a] = 1
        elif ins == 'column':
            GRID[:, a] = 1
        elif ins == 'row':
            GRID[a, :] = 1


def part2(inp):
    pass

if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1(inp))
    print(part2(inp))