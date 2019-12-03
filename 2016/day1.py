def parse(inp):
    return [(k[0], int(k[1:])) for k in inp.strip().split(', ')]

def part1(ins):
    dirs = [(1,0), (0,1), (-1,0), (0,-1)]
    x,y,direction = 0,0,0
    for lr, step in ins:
        direction += (1 if lr == 'R' else -1)
        direction %= 4
        dx, dy = dirs[direction]
        x, y = x + dx * step, y + dy * step

    return abs(x) + abs(y)

def part2(ins):
    locations = set((0,0))
    dirs = [(1,0), (0,1), (-1,0), (0,-1)]
    x,y,direction = 0,0,0
    for lr, step in ins:
        direction += (1 if lr == 'R' else -1)
        direction %= 4
        dx, dy = dirs[direction]
        for _ in range(step):
            x, y = x + dx, y + dy
            if (x,y) in locations:
                return abs(x) + abs(y)
            locations.add((x,y))

if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1(inp))
    print(part2(inp))