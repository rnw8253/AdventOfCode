import numpy as np
import sys



inputs, *blocks = open("data.dat").read().split("\n\n")

inputs = list(map(int, inputs.split(":")[1].split()))

seeds = []
for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i]+inputs[i+1]))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []
    while len(seeds) > 0:
        start, end = seeds.pop()
        for destination, source, length in ranges:
            overlapStart = max(start, source)
            overlapEnd = min(end, source+length)
            if overlapStart < overlapEnd:
                new.append((overlapStart-source+destination, overlapEnd-source+destination))
                if overlapStart > start:
                    seeds.append((start,overlapStart))
                if end > overlapEnd:
                    seeds.append((overlapEnd,end))
                break
        else:
            new.append((start, end))    
    seeds = new

print(min(seeds)[0])


