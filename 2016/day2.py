GRID = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

GRID2 = [
    [None, None, 1, None, None],
    [None, 2, 3, 4, None],
    [5, 6, 7, 8, 9],
    [None, 'A', 'B', 'C', None],
    [None, None, 'D', None, None]
]

DIRS = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

def parse(inp):
    # print(inp)
    return [k.strip() for k in inp.splitlines() if k.strip()]

def part1(ins, GRID):
    x,y = 1,1

    digits = []
    for digit in ins:
        for c in digit:
            dx, dy = DIRS[c]
            x, y = min(max(x+dx, 0), 2), min(max(y+dy, 0), 2)
            # print(dx, dy, x, y, GRID[x][y])
        digits.append(str(GRID[x][y]))
    return ''.join(digits)

def part2(ins, GRID):
    x,y = 2,0

    digits = []
    for digit in ins:
        for c in digit:
            dx, dy = DIRS[c]
            if  0 <= x + dx <= 4 and 0 <= y + dy <= 4 and GRID[x+dx][y+dy] is not None:
                x, y = x + dx, y + dy
            # print(dx, dy, x, y, GRID[x][y])
        digits.append(str(GRID[x][y]))
    return ''.join(digits)

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read()
    print(part1(parse(inp), GRID))
    print(part2(parse(inp), GRID2))
