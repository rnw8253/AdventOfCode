
class Lagoon:
    dirs = { "U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1) }
    
    def __init__(self, fname):
        self.instructions = [ instruction.split() for instruction in open(fname).read().splitlines() ]
        for i in range(len(self.instructions)):
            self.instructions[i][1] = int(self.instructions[i][1])
            self.instructions[i][2] = self.instructions[i][2][2:-1]

    def show(self):
        print(self.instructions)

    def area(self):
        points = [(0,0)]
        boundary_points = 0
        for (d, n, _) in self.instructions:
            dr, dc = Lagoon.dirs[d]
            r, c = points[-1]
            boundary_points += n
            points.append((r + dr * n, c + dc * n))

        # Use shoelace formula to get the area
        area = abs(sum(points[i][0] * (points[i -1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points))))/2
        
        # Picks theorem to get the number of interior points
        interior_points = area - boundary_points // 2 + 1

        return int(interior_points + boundary_points)

    def hex_area(self):
        points = [(0,0)]
        boundary_points = 0
        for (_, _, x) in self.instructions:
            dr, dc = Lagoon.dirs["RDLU"[int(x[-1])]]
            n = int(x[:-1], 16)
            r, c = points[-1]
            boundary_points += n
            points.append((r + dr * n, c + dc * n))

        # Use shoelace formula to get the area
        area = abs(sum(points[i][0] * (points[i -1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points))))/2
        
        # Picks theorem to get the number of interior points
        interior_points = area - boundary_points // 2 + 1

        return int(interior_points + boundary_points)

L = Lagoon("test.dat")
print(f"The area of the dig site is: {L.area()}")
print(f"The hex area of the dig site is: {L.hex_area()}")


L = Lagoon("data.dat")
print(f"The area of the dig site is: {L.area()}")
print(f"The hex area of the dig site is: {L.hex_area()}")

