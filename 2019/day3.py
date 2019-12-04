import itertools
import collections
import re
import string

def parse(inp):
    return [k.split(',') for k in inp.splitlines() if k.strip()]

def part1(inp):
    seens = []
    dirs = {'R': (0,1), 'L': (0, -1), 'U':(-1,0), 'D':(1,0)}
    intersects = []
    for wire in inp:
        x = y = 0
        seen = set()
        for ins in wire:
            direction, dist = ins[0], int(ins[1:])
            dx, dy = dirs[direction]
            for _ in range(dist):
                x += dx
                y += dy
                seen.add((x,y))
        seens.append(seen)
    intersects = seens[0] & seens[1]

    return min(abs(x)+abs(y) for (x,y) in intersects)

def part2(inp):
    seens = []
    dirs = {'R': (0,1), 'L': (0,-1), 'U':(-1,0), 'D':(1,0)}
    for wire in inp:
        x = y = 0
        seen = {}
        steps = 0
        for ins in wire:
            direction, dist = ins[0], int(ins[1:])
            dx, dy = dirs[direction]
            for _ in range(dist):
                steps += 1
                x += dx
                y += dy
                seen[(x,y)] = seen.get((x,y), steps)
        seens.append(seen)
    intersects = seens[0].keys() & seens[1].keys()

    return min(abs(x)+abs(y) for (x,y) in intersects), min(seens[0][k] + seens[1][k] for k in intersects)

if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1(inp.copy()))
    print(part2(inp.copy()))
