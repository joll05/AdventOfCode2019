f = open("input.txt")

wires = f.readlines()
wires[0] = wires[0].split(",")
wires[1] = wires[1].split(",")

maxX = input("maxX: ")
maxY = input("maxY: ")

crossedPositions = [[False] * 20000] * 20000

posX = 0
posY = 0

i = 0
for i in wires[0]:
    direction = [x=0, y=0]
