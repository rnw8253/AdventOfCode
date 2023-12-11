import numpy as np
import sys
import pandas as pd




def ParseAlmanacFile(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    nLines = len(lines)
    seedToSoil = []
    soilToFertilizer = []
    fertilizerToWater = []
    waterToLight = []
    lightToTemp = []
    tempToHumidity = []
    humidityToLocation = []
    for lineNum, line in enumerate(lines):
        if line[:7] == "seeds: ":
            seeds = line[7:].split()

        if line == "seed-to-soil map:\n":
            for lin in range(lineNum+1,nLines):
                if lines[lin] == "\n":
                    break
                temp = lines[lin].split()
                seedToSoil.append(temp)
        if line == "soil-to-fertilizer map:\n":
           for lin in range(lineNum+1,nLines):
                if lines[lin] == "\n":
                    break
                temp = lines[lin].split()
                soilToFertilizer.append(temp)
        if line == "fertilizer-to-water map:\n":
            for lin in range(lineNum+1,nLines):
                if lines[lin] == "\n":
                    break
                temp = lines[lin].split()
                fertilizerToWater.append(temp)
        if line == "water-to-light map:\n":
            for lin in range(lineNum+1,nLines):
                if lines[lin] == "\n":
                    break
                temp = lines[lin].split()
                waterToLight.append(temp)
        if line == "light-to-temperature map:\n":
            for lin in range(lineNum+1,nLines):
                if lines[lin] == "\n":
                    break
                temp = lines[lin].split()
                lightToTemp.append(temp)
        if line == "temperature-to-humidity map:\n":
            for lin in range(lineNum+1,nLines):
                if lines[lin] == "\n":
                    break
                temp = lines[lin].split()
                tempToHumidity.append(temp)
        if line == "humidity-to-location map:\n":
            for lin in range(lineNum+1,nLines):
                if lines[lin] == "\n":
                    break
                temp = lines[lin].split()
                humidityToLocation.append(temp)
        

    return seeds, seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemp, tempToHumidity, humidityToLocation



def GetConversion(inpVal, conversion):
    for conv in conversion:
        if conv[1] <= inpVal <= conv[1]+conv[2]:
            return inpVal + conv[0] - conv[1]
    return inpVal
def GetAllSeeds(seeds):
    for i in range(0,len(seeds),2):
        if i == 0:
            allSeeds = list(range(seeds[i],seeds[i]+seeds[i+1]+1))
        else:
            allSeeds += list(range(seeds[i],seeds[i]+seeds[i+1]+1))
    return allSeeds


seeds, seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemp, tempToHumidity, humidityToLocation = ParseAlmanacFile("data.dat")

seeds = np.array(seeds,int)
seeds = GetAllSeeds(seeds)
print(seeds)

seedToSoil = np.array(seedToSoil,int)
soilToFertilizer = np.array(soilToFertilizer,int)
fertilizerToWater = np.array(fertilizerToWater,int)
waterToLight = np.array(waterToLight,int)
lightToTemp = np.array(lightToTemp,int)
tempToHumidity = np.array(tempToHumidity,int)
humidityToLocation = np.array(humidityToLocation,int)



# Create pandas dataframe
data = { 'Seeds': seeds }
df = pd.DataFrame(data)
df['Soil'] = df['Seeds'].apply(GetConversion,conversion=seedToSoil) 
df['Fertilizer'] = df['Soil'].apply(GetConversion,conversion=soilToFertilizer)
df['Water'] = df['Fertilizer'].apply(GetConversion,conversion=fertilizerToWater)
df['Light'] = df['Water'].apply(GetConversion,conversion=waterToLight)
df['Temperature'] = df['Light'].apply(GetConversion,conversion=lightToTemp)
df['Humidity'] = df['Temperature'].apply(GetConversion,conversion=tempToHumidity)
df['Location'] = df['Humidity'].apply(GetConversion,conversion=humidityToLocation)

print(df.sort_values('Location'))
print("Smallest Location id: %s" %(df['Location'].min()))

