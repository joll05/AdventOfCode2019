import numpy as np

class Game:
    gridSize = (0, 0)
    alive = []

    checkLocations = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def __init__(self, startGrid):
        self.gridSize = startGrid.shape

        for x in range(startGrid.shape[0]):
            for y in range(startGrid.shape[1]):
                if(startGrid[x, y] == True):
                    self.alive += [(x, y)]
                    
    def IsAlive(self, x, y):
        return (x, y) in self.alive

    def InsideBounds(self, x, y):
        if(x < 0 or x >= self.gridSize[0] or y < 0 or y >= self.gridSize[1]):
            return False

        return True
            
    def AliveNextStep(self, x, y, currentlyAlive):
        if(not self.InsideBounds(x, y)): return False
        
        aliveCount = 0
        for i in self.checkLocations:
            location = (x + i[0], y + i[1])
            
            if(not self.InsideBounds(location[0], location[1])): continue
            
            if(self.IsAlive(location[0], location[1])):
               aliveCount += 1
               
        if(currentlyAlive):
            if(aliveCount != 1):
               return False

            return True

        # else
        if(aliveCount != 1 and aliveCount != 2):
           return False

        return True

    def Draw(self, aliveChar="#", deadChar="."):
        out = ""
        for y in range(self.gridSize[0]):
            for x in range(self.gridSize[1]):
               if((x, y) in self.alive):
                   out += aliveChar
               else:
                   out += deadChar
            out += "\n"

        return out
    
    def Step(self, count=0, draw=False):
        dead = []
        born = []
        # Note to self: dead should contain array indicies,
        # born should contain position tuples
               
        for i, bug in enumerate(self.alive):
            if(not self.AliveNextStep(bug[0], bug[1], True)):
               dead += [i]

            for l in self.checkLocations:
                location = (bug[0] + l[0], bug[1] + l[1])
                
                if(not self.IsAlive(location[0], location[1])):
                    if(not location in born):
                        if(self.AliveNextStep(location[0], location[1], False)):
                            born += [location]

        for i, d in enumerate(dead):
            self.alive.pop(d - i)

        self.alive += born

        if(count > 0): self.step(count - 1)

    def CalculateBiodiversity(self):
        total = 0
        for bug in self.alive:
            tileNumber = bug[0] + bug[1] * self.gridSize[1]
            total += pow(2, tileNumber)

        return total
