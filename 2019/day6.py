import itertools
import collections
import re
import string
import networkx as nx

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.val == other.val
        else:
            return self.val == other

    def __hash__(self):
        return hash(self.val)

def parse(inp):
    return list(k.split(')') for k in inp.splitlines() if k.strip())

def part1(inp, *args, **kwargs):
    G = nx.DiGraph()
    for a,b in inp:
        G.add_edge(a, b)
    root_node, *other_nodes = nx.topological_sort(G)
    total = 0
    for node in other_nodes:
        total += nx.shortest_path_length(G, root_node, node)
    return total

def part2(inp, *args, **kwargs):
    G = nx.Graph()
    for a,b in inp:
        G.add_edge(a, b)
    return nx.shortest_path_length(G, 'SAN', 'YOU') - 2
    
if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1(inp.copy()))
    print('=====')
    print(part2(inp.copy()))