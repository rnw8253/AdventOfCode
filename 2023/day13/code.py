
class Mirror():

    def __init__(self, pattern):
        self.rows = list(pattern.splitlines())
        self.cols = list(zip(*self.rows))

    def show(self):
        print("\n")
        print("\n".join(self.rows))

    def checkReflection(self):
        matchingRows = [r for r in range(1,len(self.rows)) if self.rows[:r][::-1][:len(self.rows)-r] == self.rows[r:][:r]]
        matchingCols = [c for c in range(1,len(self.cols)) if self.cols[:c][::-1][:len(self.cols)-c] == self.cols[c:][:c]]
        row = matchingRows[0] if len(matchingRows) > 0 else 0
        col = matchingCols[0] if len(matchingCols) > 0 else 0
        return row, col

    def checkReflectionSmudges(self):
        matchingRows = [r for r in range(1,len(self.rows)) if sum(sum(0 if a == b else 1 for a, b in zip(x,y)) for x, y in zip(self.rows[:r][::-1], self.rows[r:])) == 1]
        matchingCols = [c for c in range(1,len(self.cols)) if sum(sum(0 if a == b else 1 for a, b in zip(x,y)) for x, y in zip(self.cols[:c][::-1], self.cols[c:])) == 1]
        row = matchingRows[0] if len(matchingRows) > 0 else 0
        col = matchingCols[0] if len(matchingCols) > 0 else 0
        return row, col
        


blocks = open("test.dat").read().split("\n\n")
total = 0
total2 = 0
for block in blocks:
    m = Mirror(block)
    row, col = m.checkReflection()
    total += 100*row + col
    row, col = m.checkReflectionSmudges()
    total2 += 100*row + col
print(f"Not accounting for smudges test total: {total}")
print(f"Accounting for smudges testt otal: {total2}")

    
blocks = open("data.dat").read().split("\n\n")
total = 0
total2 = 0
for block in blocks:
    m = Mirror(block)
    row, col = m.checkReflection()
    total += 100*row + col
    row, col = m.checkReflectionSmudges()
    total2 += 100*row + col
print(f"Not accounting for smudges total: {total}")
print(f"Accounting for smudges total: {total2}")

