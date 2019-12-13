class Moon:
    position = [None, None, None]
    velocity = [None, None, None]
    
    def __init__(self, position):
        self.position = list(position)
        self.velocity = [0] * len(position)

    def ApplyGravity(self, moons):
        for moon in moons:
            for coord in range(len(moon.position)):
                if(self.position[coord] < moon.position[coord]):
                    self.velocity[coord] += 1
                elif(self.position[coord] > moon.position[coord]):
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

Moons = []

for i in data:
    coords = i[1:-2]

    coords = coords.split(", ")

    for coord in range(len(coords)):
        coords[coord] = int(coords[coord][2:])

    Moons += [Moon(coords)]

start = []

for moon in Moons:
    start += [moon.position]

def StartCheck():
    for moon in range(len(Moons)):
        if(Moons[moon].velocity != [0, 0, 0]):
            return False

        if(Moons[moon].position != start[moon]):
            return False
    
    return True

step = 0
def TimeStep():
    global Moons
    global step
    
    for moon in Moons:
        moon.ApplyGravity(Moons)

    for moon in Moons:
        moon.ApplyVelocity()

    step += 1

    if(StartCheck()):
        print("Found it at step %d" % step)
        print("Current:")
        for moon in Moons:
            print("pos: %s, vel: %s" % (moon.position, moon.velocity))
        print("Starting point:")
        for moon in start:
            print("pos: %s" % (moon))
        exit()

while True:
    TimeStep()
