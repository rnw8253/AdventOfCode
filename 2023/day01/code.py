import numpy as np
import sys

def CalcTwoDigitIntOnly(line):
    val = 0
    firstValue = 0
    lastValue = 0
    for c in line:
        if c.isdigit():
            firstValue = int(c)
            break
    for c in line[::-1]:
        if c.isdigit():
            lastValue = int(c)
            break
    
    return int("%s%s" %(firstValue,lastValue))

def CalcTwoDigit(line):
    val = 0
    firstValue = 0
    lastValue = 0
    for ind, c in enumerate(line):
        if c.isdigit():
            firstValue = int(c)
            break
        else:
            if c == "z":
                if line[ind:ind+3] == "zero":
                    firstValue = 0
                    break
            elif c == "o":
                if line[ind:ind+3] == "one":
                    firstValue = 1
                    break
            elif c == "t":
                if line[ind:ind+3] == "two":
                    firstValue = 2
                    break
                elif line[ind:ind+5] == "three":
                    firstValue = 3
                    break
            elif c == "f":
                if line[ind:ind+4] == "four":
                    firstValue = 4
                    break
                elif line[ind:ind+4] == "five":
                    firstValue = 5
                    break
            elif c == "s":
                if line[ind:ind+3] == "six":
                    firstValue = 6
                    break
                elif line[ind:ind+5] == "seven":
                    firstValue = 7
                    break
            elif c == "e":
                if line[ind:ind+5] == "eight":
                    firstValue = 8
                    break
            elif c == "n":
                if line[ind:ind+4] == "nine":
                    firstValue = 9
                    break
    backLine = line[::-1]
    for ind, c in enumerate(backLine):
        if c.isdigit():
            lastValue = int(c)
            break
        else:
            if c == "o":
                if backLine[ind:ind+4] == "orez":
                    lastValue = 0
                    break
                elif backLine[ind:ind+3] == "owt":
                    lastValue = 2
                    break
            elif c == "e":
                print(backLine[ind:ind+3])
                if backLine[ind:ind+3] == "eno":
                    lastValue = 1
                    break
                elif backLine[ind:ind+5] == "eerht":
                    lastValue = 3
                    break
                elif backLine[ind:ind+4] == "evif":
                    lastValue = 5
                    break
                elif backLine[ind:ind+4] == "enin":
                    lastValue = 9
                    break
            elif c == "r":
                if  backLine[ind:ind+4] == "ruof":
                    lastValue = 4
                    break
            elif c == "x":
                if  backLine[ind:ind+3] == "xis":
                    lastValue = 6
                    break
            elif c == "n":
                if  backLine[ind:ind+5] == "neves":
                    lastValue = 7
                    break
            elif c == "t":
                if  backLine[ind:ind+5] == "thgie":
                    lastValue = 8
                    break
    print(line)
    print(firstValue,lastValue)
    return int("%s%s" %(firstValue,lastValue))



numberDict = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}

f =open("data.dat",'r')
total = 0
for line in f:
    #total += CalcTwoDigitIntOnly(line.lower())
    total += CalcTwoDigit(line[:len(line)-1].lower())
    
print(total)
