def calc_fuel(x):
    f = 0
    while x > 0:
        x = x // 3 - 2
        if x > 0:
            f += x
    return f