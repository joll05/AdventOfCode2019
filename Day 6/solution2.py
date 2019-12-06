f = open("input.txt", "r")

puzzleInput = f.read()

YOUpath = []
SANpath = []

def FindOrbiters(name, previousPath):
    checkPos = 0
    if(name == "YOU"):
        global YOUpath
        YOUpath = previousPath
    elif(name == "SAN"):
        global SANpath
        SANpath = previousPath
    while True:
        out = puzzleInput.find(name + ")", checkPos)

        if(out == -1):
            break

        FindOrbiters(puzzleInput[out + 4:out + 7], previousPath + [name])
        
        checkPos = out + 4

FindOrbiters("COM", [])

def FindClosestCommonPoint():
    global YOUpath
    global SANpath
    
    indexi = 0
    for i in reversed(YOUpath):
        indexj = 0
        for j in reversed(SANpath):
            if(i == j):
                print(indexi + indexj)
                return
            indexj += 1
        indexi += 1

FindClosestCommonPoint()
