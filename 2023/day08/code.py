Afrom math import gcd


directions, path = open("data.dat").read().split("\n\n")
#directions, path = open("test.dat").read().split("\n\n")

pathDict = {}
for p in path.splitlines():
    key, values = p.split(" = ")
    pathDict[key] = {"L": values[1:4], "R": values[6:9]}

currentRoom = "AAA"
turnCount = 0
directionIndex = 0

while currentRoom != "ZZZ":
    currentRoom = pathDict[currentRoom][directions[directionIndex]]
    turnCount += 1
    directionIndex += 1
    if directionIndex == len(directions):
        directionIndex = 0
print(f"AAA to ZZZ turn count: {turnCount}")




### TAKES TO LONG NEED A NEW METHOD
#currentRooms = [key for key in pathDict.keys() if key.endswith("A")]
#allRoomZs = False
#turnCount = 0
#while allRoomZs == False:
#    # Move to the next room
#    currentRooms = [pathDict[room][directions[directionIndex]] for room in currentRooms]
#
#    # Change the direction index to the next direction
#    turnCount += 1
#    directionIndex += 1
#    if directionIndex == len(directions):
#        directionIndex = 0
#
#    # Check to see if every room ends with Z or not
#    allRoomZs = all(room.endswith('Z') for room in currentRooms)
#
#print(f"All **A to **Z turn count: {turnCount}")



## DETERMINE THE Z CYCLE FOR EACH ROUTE AND FIND THE LOWEST COMMMON DENOMINATOR
steps, _, *rest = open("data.dat").read().splitlines()
network = {}
for line in rest:
    pos, targets = line.split(" = ")
    network[pos] = targets[1:-1].split(", ")

positions = [key for key in network if key.endswith("A")]
    
cycles = []
for current in positions:
    cycle = []

    current_steps = steps
    step_count = 0
    first_z = None
    while True:
        while step_count == 0 or not current.endswith("Z"):
            step_count += 1
            current = network[current][0 if current_steps[0] == "L" else 1]
            current_steps = current_steps[1:] + current_steps[0]

        cycle.append(step_count)
        if first_z is None:
            first_z = current
            step_count = 0
        elif current == first_z:
            break

    cycles.append(cycle)

nums = [cycle[0] for cycle in cycles]

lcm = nums.pop()
for num in nums:
    lcm = lcm * num // gcd(lcm, num)
print(lcm)
