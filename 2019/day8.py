import itertools
import collections
import re
import string
import networkx as nx
import numpy as np
import pandas as pd

def parse(inp):
    return [int(k) for k in inp.strip()]

def part1(inp, *args, **kwargs):
    X, Y = 25,6
    grid = pd.DataFrame(np.array(inp).reshape((-1,X*Y))).T
    layer = grid.apply(lambda x: x.eq(0).sum()).sort_values().index[0]
    return grid[layer].eq(1).sum() * grid[layer].eq(2).sum()

def part2(inp, *args, **kwargs):
    X, Y = 25,6
    grid = np.array(inp).reshape((-1,Y,X))
    out = [[None]*25 for _ in range(6)]

    grid = grid
    for layer in grid:
        for i, row in enumerate(layer):
            for j, val in enumerate(row):
                v = out[i][j]
                if v is None:
                    if val == 0:
                        out[i][j] = '   '
                    elif val == 1:
                        out[i][j] = '■■ '

    return '\n'.join(''.join(row) for row in out)

if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1(inp.copy()))
    print(part2(inp.copy()))