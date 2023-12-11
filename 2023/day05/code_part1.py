import numpy as np
import sys



seeds, *blocks = open("data.dat").read().split("\n\n")

seeds = list(map(int, seeds.split(":")[1].split()))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []
    for seed in seeds:
        for destination, source, length in ranges:
            if seed in range(source, source + length):
                new.append(seed - source + destination)
                break
        else:
            new.append(seed)    

    seeds = new

print(min(seeds))
