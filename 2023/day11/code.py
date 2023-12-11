import numpy as np

class Universe:
    def __init__(self, universe):
        self.universe = universe.splitlines()
        self.empty_rows = [r for r, row in enumerate(self.universe) if "#" not in row]
        self.empty_cols = [c for c, col in enumerate(zip(*self.universe)) if "#" not in col]
        self.galaxy_positions = [(r, c) for r, row in enumerate(self.universe) for c, ch in enumerate(row) if ch == "#"] 
    def galaxy_pair_distance(self):
        distance = 0
        expansion = 1000000
        for i, (r1, c1) in enumerate(self.galaxy_positions):
            for (r2, c2) in self.galaxy_positions[i:]:
                for r in range(min(r1,r2), max(r1, r2)):
                   distance += expansion if r in self.empty_rows else 1
                for c in range(min(c1,c2), max(c1,c2)):
                   distance += expansion if c in self.empty_cols else 1
        return distance
    def show(self):
        print("Universe:")
        print("\n".join(self.universe))
        print()
        print("Galaxy Coordinates:")
        print(self.galaxy_positions)
        print()
        print("Empty Rows:")
        print(self.empty_rows)
        print()
        print("Empty Columns:")
        print(self.empty_cols)


u1Str = open("test.dat").read()
u2Str = open("data.dat").read()

u1 = Universe(u1Str)
#u1.show()
print(f"Sum of distances is {u1.galaxy_pair_distance()}")
u2 = Universe(u2Str)
#u2.show()
print(f"Sum of distances is {u2.galaxy_pair_distance()}")
