import GameOfBugs as gob
import numpy as np
import time

sleepTime = float(input("How long between steps (in seconds)? "))

f = open("input.txt", "r")

rows = f.readlines()

start = np.ndarray([len(rows), len(rows[-1])], dtype=bool)

for y, row in enumerate(rows):
    for x, char in enumerate(row):
        if(char == "#"):
            start[x, y] = True
        elif(char == "."):
            start[x, y] = False

eris = gob.Game(start)

previousLayouts = []

while True:
    eris.Step()
    result = eris.Draw()
    print(result)
    if(result in previousLayouts):
        print("Duplicate layout found! Biodiversity: %d" % eris.CalculateBiodiversity())
        break
    previousLayouts += [result]
    time.sleep(sleepTime)
