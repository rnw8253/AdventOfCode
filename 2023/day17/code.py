from heapq import heappush, heappop


class CityBlock:

    def __init__(self, fname):
        self.grid = [list(map(int, line.strip())) for line in open(fname)]

    def find_ultra_crucible_path(self):
        seen = set()
        pq = [(0, 0, 0, 0, 0, 0)]

        while pq:
            # Pop off the small hl value always
            hl, r, c, dr, dc, n = heappop(pq)

            # At the end
            if r == len(self.grid) -1 and c == len(self.grid[0]) - 1:
                return hl

            # Make sure we are in bounds
            if r < 0 or r >= len(self.grid) or c < 0 or c >= len(self.grid[0]):
                continue

            # Check to see if we have been here before
            if (r, c, dr, dc, n) in seen:
                continue

            # Add the new location to seen
            seen.add((r, c, dr, dc, n))

            # Keep going in the same direction
            if n < 10 and (dr, dc) != (0, 0):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(self.grid) and 0 <= nc < len(self.grid[0]):
                    heappush(pq, (hl + self.grid[nr][nc], nr, nc, dr, dc, n + 1))

            # Change direction
            if n >= 4 or (dr, dc) == (0, 0):
                for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                        nr = r + ndr
                        nc = c + ndc
                        if 0 <= nr < len(self.grid) and 0 <= nc < len(self.grid[0]):
                            heappush(pq, (hl + self.grid[nr][nc], nr, nc, ndr, ndc, 1))
        
        
    def find_crucible_path(self):
        seen = set()
        pq = [(0, 0, 0, 0, 0, 0)]

        while pq:
            # Pop off the small hl value always
            hl, r, c, dr, dc, n = heappop(pq)

            # At the end
            if r == len(self.grid) -1 and c == len(self.grid[0]) - 1:
                return hl

            # Make sure we are in bounds
            if r < 0 or r >= len(self.grid) or c < 0 or c >= len(self.grid[0]):
                continue

            # Check to see if we have been here before
            if (r, c, dr, dc, n) in seen:
                continue

            # Add the new location to seen
            seen.add((r, c, dr, dc, n))

            # Keep going in the same direction
            if n < 3 and (dr, dc) != (0, 0):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(self.grid) and 0 <= nc < len(self.grid[0]):
                    heappush(pq, (hl + self.grid[nr][nc], nr, nc, dr, dc, n + 1))

            # Change direction
            for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                    nr = r + ndr
                    nc = c + ndc
                    if 0 <= nr < len(self.grid) and 0 <= nc < len(self.grid[0]):
                        heappush(pq, (hl + self.grid[nr][nc], nr, nc, ndr, ndc, 1))

    def show(self):
        print(self.grid)


c = CityBlock("test.dat")
print(f"Minimum heat loss for crucible: {c.find_crucible_path()}")
print(f"Minimum heat loss for ultra crucible: {c.find_ultra_crucible_path()}")

c = CityBlock("data.dat")
print(f"Minimum heat loss for crucible: {c.find_crucible_path()}")
print(f"Minimum heat loss for ultra crucible: {c.find_ultra_crucible_path()}")

