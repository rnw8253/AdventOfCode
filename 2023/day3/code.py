import numpy as np
import sys



f = open("data.dat",'r')
# Determine all symbols that are not numbers or periods
symbols = []
for c in str(f.read().replace("\n","")):
    addFlag = True
    if c != "." and not c.isdigit(): 
        for symbol in symbols:
            if symbol == c:
                addFlag = False
        if addFlag:
            symbols.append(c)


# Determine each number and its row index and its starting and stopping column index
f.seek(0)
nRows = sum(1 for line in f)
f.seek(0)
lines = f.readlines()
numbers = []
for rowNum, row in enumerate(lines):
    inNumber = False
    for columnNumber, column in enumerate(row):
        if column.isdigit():
            if not inNumber:
                startColumn = int(columnNumber)
                inNumber = True
        else:
            if inNumber:
                stopColumn = int(columnNumber-1)
                inNumber =False
                numbers.append([row[startColumn:stopColumn+1],rowNum,startColumn,stopColumn])
        if columnNumber == len(row):
            if inNumber:
                stopColumn = columnNumber
                inNumber =False
                numbers.append([row[startColumn,stopColumn+1],rowNum,startColumn,stopColumn])


numbers = np.array(numbers, dtype = int)       


# Get all numbers next to a symbol
#validNumbers = []
#for numberIndex, number in enumerate(numbers):
#    for index in range(number[2]-1, number[3]+2):
#        if str(lines[number[1]][index]) in symbols:
#            validNumbers.append(number[0])
#            break
#        if number[1] != nRows-1:
#            if lines[number[1]+1][index] in symbols:
#                validNumbers.append(number[0])
#                break
#        if number[1] != 0:
#            if lines[number[1]-1][index] in symbols:
#                validNumbers.append(number[0])
#                break
#        
#print(np.sum(validNumbers))


# Get all numbers next to a '*'
validNumbers = []
symbols = ["*"]
print(symbols)
for numberIndex, number in enumerate(numbers):
    for index in range(number[2]-1, number[3]+2):
        if str(lines[number[1]][index]) in symbols:
            validNumbers.append([number[0],number[1],index])
            break
        if number[1] != nRows-1:
            if lines[number[1]+1][index] in symbols:
                validNumbers.append([number[0],number[1]+1,index])
                break
        if number[1] != 0:
            if lines[number[1]-1][index] in symbols:
                validNumbers.append([number[0],number[1]-1,index])
                break

# Get Unique Gears
validNumbers = np.array(validNumbers,int)
uniqueGears = []
for number in validNumbers:
    addGear = True
    for gear in uniqueGears:
        if number[1] == gear[0] and number[2] == gear[1]:
            addGear = False
    if addGear:
        uniqueGears.append([number[1],number[2]])

# Get numbers for gears with more than one number by it
gearNumbers = []
for gear in uniqueGears:
    temp = []
    for number in validNumbers:
        if gear[0] == number[1] and gear[1] == number[2]:
            temp.append(number[0])
    if len(temp)>1:
        gearNumbers.append(temp)

# mulitiply and add
total = 0
for gear in gearNumbers:
    val = 1
    for num in gear:
        val *= num
    total += val
print(total)
#print(numbers)
#for row in range(nRows):
#    print(numbers[numbers[:,1] == row])
