import numpy as np

def manhattan(point):
    return abs(point[0]) + abs(point[1])

f = open("input.txt", "r")

data = f.readlines()

size = (len(data[0]) - 2, len(data))

asteroids = []

for y in range(len(data)):
    line = data[y][:-2]
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

    hiddenTiles = np.empty((100, 100), dtype=bool)
