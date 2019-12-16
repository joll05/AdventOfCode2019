import computer
import numpy as np
import time

Position = (0, 0)

Canvas = np.full([200, 200], -1, dtype=int)
Canvas[0, 0] = 1

Corners = [(0, 0), (0, 0)]

TileCount = 0

Direction = 0

def AddVectors(vec1, vec2):

    if(len(vec1) != len(vec2)):
        return None

    out = []
    for v in range(len(vec1)):
        out += [vec1[v] + vec2[v]]

    return tuple(out)

def SendInput():
    global Canvas
    global Position
    
    if(Canvas[Position] == 1):
        return 1
    else:
        return 0

def MoveRobot():
    global Direction
    global Position
    global Corners
    
    if(Direction == 0):
        Position = AddVectors(Position, (0, 1))
    elif(Direction == 1):
        Position = AddVectors(Position, (1, 0))
    elif(Direction == 2):
        Position = AddVectors(Position, (0, -1))
    elif(Direction == 3):
        Position = AddVectors(Position, (-1, 0))

    print(Position)

    if(Position[0] < Corners[0][0] or Position[1] < Corners[0][1]):
        Corners[0] = Position
    elif(Position[0] > Corners[1][0] or Position[1] > Corners[1][1]):
        Corners[1] = Position

Turning = False
def RecieveOutput(out):
    global Turning
    global Direction
    global Canvas
    global Position
    global TileCount
    
    if(not Turning):
        if(Canvas[Position] == -1):
            TileCount += 1
        Canvas[Position] = out
    else:
        if(out == 0):
            Direction -= 1
        else:
            Direction += 1

        if(Direction < 0):
            Direction += 4
        elif(Direction > 3):
            Direction -= 4

        MoveRobot()

    Turning = not Turning

computer.Run(RecieveOutput, SendInput)

blackChar = u"\u25A0"
whiteChar = u"\u25A1"

for x in range(Corners[0][0] - 1, Corners[1][0] + 2):
    out = ""
    for y in range(Corners[0][1] - 1, Corners[1][1] + 2):
        if(Canvas[x, y] == 1):
            out += whiteChar
        else:
            out += blackChar
    print(out)
    time.sleep(0.2)
