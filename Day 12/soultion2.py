import time

class Moon:
    position = [None, None, None]
    velocity = [None, None, None]
    
    def __init__(self, position):
        self.position = list(position)
        self.velocity = [0] * len(position)

    def ApplyGravity(self, ms):
        for m in ms:
            for coord in range(len(m.position)):
                if(self.position[coord] < m.position[coord]):
                    self.velocity[coord] += 1
                elif(self.position[coord] > m.position[coord]):
                    self.velocity[coord] -= 1

    def ApplyVelocity(self):
        for coord in range(len(self.velocity)):
            self.position[coord] += self.velocity[coord]

    def GetEnergy(self):
        pot = 0
        for pos in self.position:
            pot += abs(pos)
            
        kin = 0
        for vel in self.velocity:
            kin += abs(vel)

        return pot * kin

f = open("input.txt")

data = f.readlines()

def ProcessData():
    out = []
    for i in data:
        coords = i[1:-2]

        coords = coords.split(", ")

        for coord in range(len(coords)):
            coords[coord] = int(coords[coord][2:])

        out += [Moon(coords)]
    return out

Moons = ProcessData()

start = ProcessData()

def StartCheck():
    for m in range(len(start)):
        if(Moons[m].velocity != [0, 0, 0]):
            return False
        
        if(Moons[m].position != start[m].position):
            return False
    
    return True

step = 0
def TimeStep():
    global Moons
    global step
    
    for m in Moons:
        m.ApplyGravity(Moons)

    for m in Moons:
        m.ApplyVelocity()

    step += 1

    if(step % 50000 == 0):
        print(step)

    if(StartCheck()):
        print("Found it at step %d" % step)
        while True:
            time.sleep(1)

while True:
    TimeStep()
