from collections import deque


class MirrorGrid:

    def __init__(self, fname):
        self.grid = open(fname).read().splitlines()

    def maxEnergizedTiles(self):
        max_val = 0
        for r in range(len(self.grid)):
            max_val = max(max_val, self.energizedTiles(r, -1, 0, 1))
            max_val = max(max_val, self.energizedTiles(r, len(self.grid[0]), 0, -1))
        for c in range(len(self.grid)):
            max_val = max(max_val, self.energizedTiles(-1, c, 1, 0))
            max_val = max(max_val, self.energizedTiles(len(self.grid), c, -1, 0))
        return max_val
        
    def energizedTiles(self, r = 0, c = -1, dr = 0, dc = 1):
        a = [(r, c, dr, dc)]
        seen = set()
        q = deque(a)

        while q:
            r, c, dr, dc = q.popleft()
            
            r += dr
            c += dc

            if r < 0 or r >= len(self.grid) or c < 0 or c >= len(self.grid[0]):
                continue

            ch = self.grid[r][c]

            if ch == "." or (ch == "-" and dc != 0) or (ch == "|" and dr != 0):
                if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))

            elif ch =="/":
                dr, dc = -dc, -dr
                if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))

            elif ch =="\\":
                dr, dc = dc, dr
                if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))

            else:
                for dr, dc in [(1,0), (-1, 0)] if ch =="|" else [(0, 1), (0, -1)]:
                    if (r, c, dr, dc) not in seen:
                        seen.add((r, c, dr, dc))
                        q.append((r, c, dr, dc))    
                
        coords = {(r, c) for (r, c, _, _) in seen}
        return len(coords)

m = MirrorGrid('test.dat')
print(m.energizedTiles())
print(m.maxEnergizedTiles())
m = MirrorGrid('data.dat')
print(m.energizedTiles())
print(m.maxEnergizedTiles())
