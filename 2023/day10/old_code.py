
pipes = open("data.dat").read().split("\n")

def FindBothPaths(start):
    connections = []
    if start[0] != 0:
        if pipes[start[0]-1][start[1]] in "F7|":
            connections.append([start[0]-1,start[1]])
    if start[0] != nRows-1:
        if pipes[start[0]+1][start[1]] in "LJ|":
            connections.append([start[0]+1,start[1]])
    if start[1] != 0:
        if pipes[start[0]][start[1]-1] in "FL-":
            connections.append([start[0],start[1]-1])
    if start[1] != nCols - 1:
        if pipes[start[0]][start[1]+1] in "J7-":
            connections.append([start[0],start[1]+1])
    return connections

def FindNextPath(tile, prev_path):
    currentPipe = pipes[tile[0]][tile[1]]
    if currentPipe == "-":
        if tile[1]-1 == prev_path[1]:
            return [tile[0], tile[1]+1], tile
        else:
            return [tile[0], tile[1]-1], tile
    elif currentPipe == "|":
        if tile[0]-1 == prev_path[0]:
            return [tile[0]+1, tile[1]], tile
        else:
            return [tile[0]-1, tile[1]], tile
    elif currentPipe == "J":
        if tile[0]-1 == prev_path[0]:
            return [tile[0],tile[1]-1], tile
        else:
            return [tile[0]-1,tile[1]], tile
    elif currentPipe == "L":
        if tile[0]-1 == prev_path[0]:
            return [tile[0],tile[1]+1], tile
        else:
            return [tile[0]-1,tile[1]], tile
    elif currentPipe == "7":
        if tile[0]+1 == prev_path[0]:
            return [tile[0],tile[1]-1], tile
        else:
            return [tile[0]+1,tile[1]], tile
    elif currentPipe == "F":
        if tile[0]+1 == prev_path[0]:
            return [tile[0],tile[1]+1], tile
        else:
            return [tile[0]+1,tile[1]], tile
    
    else:
        return tile, prev_path


nRows = len(pipes)
nCols = len(pipes[0])

start = [0, 0]
for rowNum, row in enumerate(pipes):    
    for colNum, col in enumerate(row):
        if col == "S":
            start = [rowNum, colNum]
            break


# Part 1
paths = FindBothPaths(start)
prev_paths = [start,start]
steps = 1
while paths[0] != paths[1]:
    for i in range(len(paths)):
        paths[i], prev_paths[i] = FindNextPath(paths[i],prev_paths[i])
    steps += 1
print(steps)

# Part 2: Determine the number of times spot crosses pipe to get to the edge (even = outside, odd = inside)

# Determine what S must be

# Replace S and replace not used pipes with .

# loop over all pipes
