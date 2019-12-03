import itertools
import collections
import re
import string

def parse(inp):
    return list(map(int, inp.splitlines()))

def part1(inp):
    return sum(k//3 - 2 for k in inp)

def part2(inp):
    s = 0
    for k in inp:
        while k >= 0:
            k = k // 3 - 2
            if k > 0:
                s += k
    return s

if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1(inp))
    print(part2(inp))