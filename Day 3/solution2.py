import numpy as np

def manhattan(x, y):
    return abs(x) + abs(y)

f = open("input.txt")

wires = f.readlines()
wires[0] = wires[0].split(",")
wires[1] = wires[1].split(",")

max = int(input("Max: "))

crossedPositions = np.zeros((max, max), dtype=int)

shortestDistance = 999999

posX = 0
posY = 0

checkingMode = False
for wire in wires:
    posX = 0
    posY = 0

    totalSteps = 0
    for i in wire:
        direction = i[0]

        for step in range(int(i[1:])):
            totalSteps += 1

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
                if(crossedPositions[posX, posY] != 0):
                    if(crossedPositions[posX, posY] + totalSteps < shortestDistance):
                        shortestDistance = crossedPositions[posX, posY] + totalSteps
            elif(crossedPositions[posX, posY] == 0):
                crossedPositions[posX, posY] = totalSteps

    checkingMode = True

print(shortestDistance)
