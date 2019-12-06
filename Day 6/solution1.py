f = open("input.txt", "r")

puzzleInput = f.read()

totalOrbitCount = 0

def FindOrbiters(name, orbitCount):
    global totalOrbitCount
    
    totalOrbitCount += orbitCount
    checkPos = 0
    while True:
        out = puzzleInput.find(name + ")", checkPos)

        if(out == -1):
            break

        FindOrbiters(puzzleInput[out + 4:out + 7], orbitCount + 1)
        
        checkPos = out + 4

FindOrbiters("COM", 0)

print(totalOrbitCount)
