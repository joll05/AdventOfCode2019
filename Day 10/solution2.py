import math

def manhattan(point):
    return abs(point[0]) + abs(point[1])

def getAngle(point, sorting=True):
    result = 0
    result += (math.degrees(math.atan2(point[1], point[0])) + 180 - 90) % 360
    if(sorting):
        result += manhattan(point) / 1000
    
    return result

def truncate(N, decimals):    
    num = N * (10 ** decimals)
    num = math.trunc(num)
    return num / (10 ** decimals)

f = open("input.txt", "r")

data = f.readlines()

asteroids = []

station = (20, 19)

for y in range(len(data)):
    line = data[y]
    for x in range(len(line)):
        char = line[x]
        if(char == "#"):
            asteroids += [(x, y)]

asteroids_sorted = []

for i in asteroids:
    asteroids_sorted += [(i[0] - station[0], i[1] - station[1])]

asteroids_sorted.sort(key=getAngle)
asteroids_sorted.pop(0)

decimals = 1

laserAngle = 0
asteroidIndex = 0
destruction = 0
while True:
    asteroid = asteroids_sorted[asteroidIndex % len(asteroids_sorted)]
    asteroidAngle = truncate(getAngle(asteroid, False), decimals)

    if(asteroidAngle < laserAngle):
        asteroidIndex += 1
    else:
        if(asteroidAngle == laserAngle):
            destruction += 1
            if(destruction == 200):
                asteroid = (asteroid[0] + station[0], asteroid[1] + station[1])
                print("200th asteroid at %s. X * 100 + Y = %d" % (asteroid, asteroid[0] * 100 + asteroid[1]))
                break
            
            asteroids_sorted.pop(asteroidIndex)
            

        laserAngle += 10 ** -decimals
        laserAngle = round(laserAngle, decimals)
        laserAngle %= 360
