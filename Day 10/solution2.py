import numpy as np

def manhattan(point):
    return abs(point[0]) + abs(point[1])

f = open("input.txt", "r")

data = f.readlines()

asteroids = []

stationPos = (20, 19)

for y in range(len(data)):
    line = data[y]
    for x in range(len(line)):
        char = line[x]
        if(char == "#"):
            asteroids += [(x, y)]

for station in asteroids:
    asteroids_sorted = []

    for i in asteroids:
        asteroids_sorted += [(i[0] - station[0], i[1] - station[1])]

    asteroids_sorted.sort(key=manhattan)
    asteroids_sorted.pop(0)

    hiddenTiles = np.full((100, 100), False, dtype=bool)

    asteroidCount = 0

    for asteroid in asteroids_sorted:
        if(hiddenTiles[asteroid] == True):
            continue

        asteroidCount += 1

        direction = divideVector(asteroid, manhattan(asteroid))

        i = 1
        while True:
            target = multiplyVector(direction, i)
            
            if(vectorIsInteger(target)):
                hiddenTiles[vectorInt(target)] = True

            if(manhattan(target) > 50):
                break

            i += 1

    if(asteroidCount > bestAsteroidCount):
        bestStation = station
        bestAsteroidCount = asteroidCount

    print("Station %s: %d asteroids visible." % (station, asteroidCount))

print("Best: %s (%d asteroids)" % (bestStation, bestAsteroidCount))
