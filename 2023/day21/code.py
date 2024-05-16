from collections import deque
import numpy as np


class Garden:

    def __init__(self, fname):
        self.garden = open(fname).read().splitlines()
        # Find the start space:
        self.start = (0, 0)
        for r, row in enumerate(self.garden):
            for c, ch in enumerate(row):
                if ch == "S":
                    self.start = (r, c)

    def __repr__(self):
        return "\n".join(self.garden)

    def walk(self, steps):
        q = deque([(self.start, 0)])
        seen = set()
        while q:
            print(q)
            pos, count = q.popleft()
            if (pos, count) not in seen:
                for move in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    newPos = np.add(pos,move)
                    if (0 <= newPos[0] < len(self.garden[0])) and (0 <= newPos[1] < len(self.garden)):
                        if count < steps:
                            q.append((newPos, count+1))

            seen.add((pos, count))
            print(seen)
            return(seen)
    
g = Garden("test.dat")
print(g.walk(64))

