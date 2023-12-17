

class Platform:
    def __init__(self,fname):
        self.grid = tuple(open(fname).read().splitlines())
    def show(self):
        print("\n\n")
        print("\n".join(self.grid))

    def tilt_north(self):
        self.grid = list(map("".join, zip(*self.grid)))
        self.grid = ["#".join(["".join(sorted(list(group), reverse = True)) for group in row.split('#')]) for row in self.grid]
        self.grid = list(map("".join, zip(*self.grid)))

        
    def cycle(self):
        for _ in range(4):
            self.grid = tuple(map("".join, zip(*self.grid)))
            self.grid = tuple("#".join(["".join(sorted(list(group), reverse = True)) for group in row.split('#')]) for row in self.grid)
            self.grid = tuple(row[::-1] for row in self.grid)

    def runCycles(self,nCycles):
        seen = {self.grid}
        array = [self.grid]
        iter = 0
        # Find the point at which we hit a loop and the offset before we hit it
        while True:
            iter += 1
            self.cycle()
            if self.grid in seen:
                break
            seen.add(self.grid)
            array.append(self.grid)
        first = array.index(self.grid)

        # Get the final grid
        self.grid = array[(nCycles - first) % (iter - first) + first]
        
    def load(self):
        return sum(row.count("O") * (len(self.grid) - r) for r, row in enumerate(self.grid))

p = Platform("test.dat")
#p.tilt_north()
p.runCycles(1000000000)
print(f"The load is {p.load()}")


p = Platform("data.dat")
#p.tilt_north()
p.runCycles(1000000000)
print(f"The load is {p.load()}")
