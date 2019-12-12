import numpy as np
import math

def manhattan(point):
    return abs(point[0]) + abs(point[1])

def getAngle(point, sorting=True):
    result = 0
    result += (math.degrees(math.atan2(point[1], point[0])) + 180 - 90) % 360
    if(sorting):
        result += manhattan(point) / 100

    return result

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

laserAngle = 0
currentAsteroid = 0
destructionCount = 0

while True:
    asteroid = asteroids_sorted[currentAsteroid]
    asteroidAngle = int(getAngle(asteroid, False))
    if(asteroidAngle < laserAngle):
        currentAsteroid += 1
        currentAsteroid = currentAsteroid % len(asteroids_sorted)

        if(int(getAngle(asteroids_sorted[currentAsteroid], False)) < asteroidAngle):
            laserAngle += 1
    elif(asteroidAngle == laserAngle):
        destructionCount += 1
        if(destructionCount == 200):
            lastAsteroid = (asteroid[0] + station[0], asteroid[1] + station[1])
            print("%s is no. 200. (%d * 100 + %d = %d)" % (lastAsteroid, lastAsteroid[0], lastAsteroid[1], lastAsteroid[0] * 100 + lastAsteroid[1]))
            break
        asteroids_sorted.pop(currentAsteroid)
        laserAngle += 1
    else:
        laserAngle += 1

    laserAngle = laserAngle % 360

    print(laserAngle)
