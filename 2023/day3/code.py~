import numpy as np
import sys

def GetGameTrials(line):
    nCubes = []
    line = line.replace("\n","")
    temp = line.split(": ")
    gameNumber = temp[0].split(" ")[1]
    temp = temp[1].split("; ")
    for game,t in enumerate(temp):
        trial = t.split(", ") 
        nRed = 0
        nBlue = 0
        nGreen = 0
        for color in trial:
            temp2 = color.split(" ")
            print(temp2)
            if temp2[1] == "red":
                nRed = int(temp2[0])
            if temp2[1] == "blue":
                nBlue = int(temp2[0])
            if temp2[1] == "green":
                nGreen = int(temp2[0])
        nCubes.append([nRed,nBlue,nGreen])
    return int(gameNumber), nCubes
        
def CheckIfValid(line):
    gameNumber, nCubes = GetGameTrials(line)
    isValid = True
    for trial in nCubes:
        for ind, val in enumerate(trial):
            if val > maxValues[ind]:
                isValid = False
    return gameNumber, isValid

def GetGamePower(line):
    gameNumber, nCubes = GetGameTrials(line)
    largeBlue = 0
    largeRed = 0
    largeGreen = 0
    for trial in nCubes:
        if trial[0] > largeRed:
            largeRed = trial[0]
        if trial[1] > largeBlue:
            largeBlue = trial[1]
        if trial[2] > largeGreen:
            largeGreen = trial[2]
    print(line)
    print(nCubes)
    print(largeRed,largeBlue,largeGreen)
    print(largeRed*largeBlue*largeGreen)
    return largeRed*largeBlue*largeGreen

maxValues = [12,14,13]    
f =open("data.dat",'r')
total = 0
totalPower = 0
for line in f:
    gameNumber, isValid = CheckIfValid(line.replace("\n",""))
    #if isValid:
    #    total += gameNumber
    totalPower += GetGamePower(line)
print(total)
print(totalPower)
