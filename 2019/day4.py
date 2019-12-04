import itertools
import collections
import re
import string

def parse(inp):
    return [int(k) for k in inp.strip().split('-')]

def part1(a,b):
    return sum(list(n) == sorted(n) and len(set(n)) < len(n) for n in map(str, range(max(100000, a), min(999999, b)+1)))

def part2(a,b):
    return sum(list(n) == sorted(n) and 2 in collections.Counter(n).values() for n in map(str, range(max(100000, a), min(999999, b)+1)))

if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1(*inp.copy()))
    print(part2(*inp.copy()))

