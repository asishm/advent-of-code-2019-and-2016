import itertools
import collections
import re
import string
import networkx as nx

def parse(inp):
    return list(k.split(')') for k in inp.splitlines() if k.strip())

def part1(inp, *args, **kwargs):
    G = nx.from_edgelist(inp)
    return sum(nx.shortest_path_length(G, 'COM').values())

def part2(inp, *args, **kwargs):
    G = nx.from_edgelist(inp)
    return nx.shortest_path_length(G, 'SAN', 'YOU') - 2
    
if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1(inp.copy()))
    print('=====')
    print(part2(inp.copy()))
