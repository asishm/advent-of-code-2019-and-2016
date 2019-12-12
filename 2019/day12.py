import math
import collections
import itertools
import string
import re

class Point:
    id_ = 0
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0
        self.modifiers = [0, 0, 0]
        self.id_ = Point.id_
        Point.id_ += 1

    def apply_gravity(self, other):
        if self.x != other.x:
            modifier = 1 if self.x < other.x else -1
            self.modifiers[0] += modifier
            other.modifiers[0] -= modifier
        if self.y != other.y:
            modifier = 1 if self.y < other.y else -1
            self.modifiers[1] += modifier
            other.modifiers[1] -= modifier
        if self.z != other.z:
            modifier = 1 if self.z < other.z else -1
            self.modifiers[2] += modifier
            other.modifiers[2] -= modifier

    def apply_gravity_modifier(self):
        self.vel_x += self.modifiers[0]
        self.vel_y += self.modifiers[1]
        self.vel_z += self.modifiers[2]
        self.modifiers = [0, 0, 0]

    def apply_velocity(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.z += self.vel_z

    def calc_kinetic(self):
        return abs(self.vel_x) + abs(self.vel_y) + abs(self.vel_z)
    
    def calc_potential(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def calc_energy(self):
        return self.calc_kinetic() * self.calc_potential()

    def __str__(self):
        return f"ID={self.id_} pos=<{self.x}, {self.y}, {self.z}> vel=<{self.vel_x}, {self.vel_y}, {self.vel_z}>"

def parse(inp):
    pat = re.compile(r"-?\d+")
    return [Point(*map(int, pat.findall(k))) for k in inp.strip().splitlines()]

class System:
    def __init__(self, planets):
        self.planets = planets

    def simulate_one(self, debug=False):
        for planet_a, planet_b in itertools.combinations(self.planets, 2):
            planet_a.apply_gravity(planet_b)
        for planet in self.planets:
            planet.apply_gravity_modifier()
            planet.apply_velocity()
        if debug:
            for planet in self.planets:
                print(planet)

    def calc_energy(self):
        return sum(planet.calc_energy() for planet in self.planets)

def part1(inp):
    system = System(inp)
    # for planet in system.planets:
    #     print(planet)
    # print("******8")
    for _ in range(1000):
        system.simulate_one()
        # print("======")
    return system.calc_energy()

def part2(inp):
    system = System(inp)
    states = [None] * 3
    counts = [0] * 3
    states[0] = tuple(planet.x for planet in system.planets) + tuple(planet.vel_x for planet in system.planets)
    states[1] = tuple(planet.y for planet in system.planets) + tuple(planet.vel_y for planet in system.planets)
    states[2] = tuple(planet.z for planet in system.planets) + tuple(planet.vel_z for planet in system.planets)
    count = 0

    while not all(counts):
        system.simulate_one()
        count += 1
        a = tuple(planet.x for planet in system.planets) + tuple(planet.vel_x for planet in system.planets)
        if a == states[0] and counts[0] == 0:
            counts[0] = count
        b = tuple(planet.y for planet in system.planets) + tuple(planet.vel_y for planet in system.planets)
        if b == states[1] and counts[1] == 0:
            counts[1] = count
        c = tuple(planet.z for planet in system.planets) + tuple(planet.vel_z for planet in system.planets)
        if c == states[2] and counts[2] == 0:
            counts[2] = count

    out = 1
    for v in counts:
        g = math.gcd(out, v)
        out *= (v // g)
    return out

if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1(inp.copy()))
    print(part2(inp.copy()))