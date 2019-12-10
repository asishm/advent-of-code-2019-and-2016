import itertools
import collections
import re
import string
import networkx as nx
from fractions import gcd
import math

def parse(inp):
    grid = [list(k) for k in inp.strip().splitlines()]
    return grid

def calc_angle(x1, y1, x2, y2):
    if x1 == x2:
        return (y1 - y2) // abs(y1 - y2), 0
    elif y1 == y2:
        return 0, (x1 - x2) // abs(x1 - x2)
    a, b = y1 - y2, x1 - x2
    common = abs(gcd(a, b))
    return (a // common, b // common)

def calc_dist(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def part1(inp):
    
    max_seen = float('-inf')
    out_coord = None
    
    for i, row in enumerate(inp):
        for j, val in enumerate(row):
            if val != '#':
                continue
            dirs = set()
            for k, row2 in enumerate(inp):
                for l, val2 in enumerate(row2):
                    if val2 != '#' or (i,j) == (k,l):
                        continue
                    los = calc_angle(i,j,k,l)
                    dirs.add(los)
            # print(f"{i,j} - {len(dirs)}, {dirs}")
            if len(dirs) > max_seen:
                out_coord = (i, j)
                max_seen = max(max_seen, len(dirs))
    return max_seen, out_coord

def part2(inp, X=19, Y=23):
    counts = collections.defaultdict(int)
    array = []
    for i, row in enumerate(inp):
        for j, val in enumerate(row):
            if val != "#" or (i,j) == (X,Y):
                continue
            deg = math.degrees(math.atan2(X-i,j-Y))

            dist = calc_dist(i,j,X,Y)
            if deg < 0: deg += 360
            counts[deg] += 1
            if 0 <= deg <= 90:
                array.append((counts[deg], 0, 90 - deg, dist, i, j))
            elif 270 <= deg < 360:
                array.append((counts[deg], 1, 360 - deg, dist, i, j))
            elif 180 <= deg < 270:
                array.append((counts[deg], 2, 270 - deg, dist, i, j))
            else:
                array.append((counts[deg], 3, 180 - deg, dist, i, j))
    
    array.sort()
    print(array)
    coord = array[199]
    return coord[5] * 100 + coord[4]

if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    part1_res, (x,y) = part1(inp.copy())
    print(part1_res, x, y)
    print("=========")
    print(part2(inp.copy(), x, y))