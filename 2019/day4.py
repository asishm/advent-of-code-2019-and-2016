import itertools
import collections
import re
import string

def parse(inp):
    return [int(k) for k in inp.strip().split('-')]

def part1(inp):
    count = 0
    a = max(100000, inp[0])
    b = min(999999, inp[1])
    for val in range(a, b + 1):
        strval = str(val)
        if list(strval) == sorted(strval) and any(k > 1 for k in collections.Counter(strval).values()): 
            # second condition works without itertools.groupby because
            # first condition would be false in a case like 112211 so we can just use a Counter
            # otherwise the check would be any(len(list(grp)) > 1 for k,grp in itertools.groupby(strval))
            count += 1
    return count

def part2(inp):
    count = 0
    a = max(100000, inp[0])
    b = min(999999, inp[1])
    for val in range(a, b + 1):
        strval = str(val)
        if list(strval) == sorted(strval) and any(k == 2 for k in collections.Counter(strval).values()): 
            # second condition works without itertools.groupby because
            # first condition would be false in a case like 112211 so we can just use a Counter
            # otherwise the check would be any(len(list(grp)) == 2 for k,grp in itertools.groupby(strval))
            count += 1
    return count

if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1(inp.copy()))
    print(part2(inp.copy()))

