

class PartSorter:

    def __init__(self,fname):
        instructions, parts = open(fname).read().split("\n\n")
        instructions = instructions.splitlines()
        self.instructions = {}
        for ins in instructions:
            label, commands = ins[:-1].split("{")
            rules = commands.split(",")
            self.instructions[label] = ([], rules.pop())
            for rule in rules:
                comparison, target = rule.split(":")
                key = comparison[0]
                comp = comparison[1]
                val = int(comparison[2:])
                self.instructions[label][0].append((key, comp, val, target))

        self.parts = []
        for part in parts.splitlines():
            item = {}
            for segment in part[1:-1].split(","):
                ch, n = segment.split("=")
                item[ch] = int(n)
            self.parts.append(item)

        self.ops = {">": int.__gt__,"<": int.__lt__}

    def printInstructions(self):
        for i in self.instructions.items():
            print(i)
            
    def accept(self, part, label):
        # if rejected
        if label == "R":
            return False
        # if accepted
        if label == "A":
            return True
        # check condition and follow outcome
        rules, fallback = self.instructions[label]
        for key, comp, n, target in rules:
            # parts[key] < n == int.__lt__(parts[key], n)
            if self.ops[comp](part[key], n):
                return self.accept(part, target)
        # if reach end do last value
        return self.accept(part, fallback)
            
    def totalAccepted(self):
        total = 0
        for part in self.parts:
            if self.accept(part, "in"):
                total += sum(part.values())
        return total


    def count(self,ranges, label = "in"):
        if label == "R":
            return 0
        if label == "A":
            product = 1
            for lo, hi in ranges.values():
                product *= hi - lo + 1
            return product

        rules, fallback = self.instructions[label]

        total = 0
        for key, comp, n, target in rules:
            lo, hi = ranges[key]
            if comp == "<":
                T = (lo, n - 1)
                F = (n, hi)
            if comp == ">":
                T = (n + 1, hi)
                F = (lo, n)
            if T[0] <= T[1]:
                copy = dict(ranges)
                copy[key] = T
                total += self.count(copy, target)
            if F[0] <= F[1]:
                ranges = dict(ranges)
                ranges[key] = F
            else:
                break
        else:
            total += self.count(ranges, fallback)

        return total
                
    def totalAccepts(self):
        return(self.count({key: (1, 4000) for key in "xmas"}))
        
p = PartSorter("test.dat")
print(f"Sum of accepted parts: {p.totalAccepted()}")
print(f"Total possible acceptable numbers: {p.totalAccepts()}")

p = PartSorter("data.dat")
print(f"Sum of accepted parts: {p.totalAccepted()}")
print(f"Total possible acceptable numbers: {p.totalAccepts()}")

