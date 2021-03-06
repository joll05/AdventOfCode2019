import numpy as np

def manhattan(x, y):
    return abs(x) + abs(y)

f = open("input.txt")

wires = f.readlines()
wires[0] = wires[0].split(",")
wires[1] = wires[1].split(",")

max = int(input("Max: "))

crossedPositions = np.zeros((max, max), dtype=bool)

closestCrossing = [999999, 999999]

posX = 0
posY = 0

checkingMode = False
for wire in wires:
    posX = 0
    posY = 0

    for i in wire:
        direction = i[0]

        for step in range(int(i[1:])):
            if(direction == "R"):
                posX += 1
            elif(direction == "L"):
                posX -= 1
            elif(direction == "U"):
                posY += 1
            elif(direction == "D"):
                posY -= 1
            else:
                print("Something went wrong.")

            if(checkingMode):
                if(crossedPositions[posX, posY] == True):
                    if(manhattan(closestCrossing[0], closestCrossing[1]) > manhattan(posX, posY)):
                        closestCrossing = [posX, posY]
            else:
                crossedPositions[posX, posY] = True

    checkingMode = True

print(manhattan(closestCrossing[0], closestCrossing[1]))
