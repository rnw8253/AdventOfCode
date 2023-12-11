import numpy as np




def CalculateWaysToWin(timeHeld,recordDistance):
    high = np.floor((timeHeld + np.sqrt(timeHeld*timeHeld - 4*recordDistance))/2)
    low = np.ceil((timeHeld - np.sqrt(timeHeld*timeHeld - 4*recordDistance))/2)
    if high*low == recordDistance:
        return (high - 1) - (low + 1) + 1 
    else :
        return high - low + 1

# Read lines    
lines = open("data.dat").read().split("\n")


# Part 1
times = list(map(int, lines[0].split(":")[1].split()))
distances = list(map(int, lines[1].split(":")[1].split()))
moe = 1
for i in range(len(times)):
    moe *= CalculateWaysToWin(times[i],distances[i])
print(f"Margin of error: {int(moe)}")


# Part 2
time = int(lines[0].split(":")[1].replace(" ",""))
distance = int(lines[1].split(":")[1].replace(" ",""))
print(f"Ways to win {int(CalculateWaysToWin(time,distance))}")
