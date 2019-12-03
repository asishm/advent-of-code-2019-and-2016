def calc_fuel(x):
    f = 0
    while x > 0:
        x = x // 3 - 2
        if x > 0:
            f += x
    return f

def parse(inp):
    return list(map(int, inp.splitlines()))

if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())

    import multiprocessing as mp
    with mp.Pool(processes=None) as pool:
        results = pool.map(calc_fuel, inp)
    print(sum(results))