import math

f = open("input.txt", "r")

data = []

pattern = [0, 1, 0, -1]

for char in f.read():
    data += [int(char)]

data *= 10000

outputOffset = ""

for i in range(7):
    outputOffset += str(data[i])

outputOffset = int(outputOffset)

for loop in range(100):
    for i in range(outputOffset + 9):
        total = 0
        for x, dat in enumerate(data):
            total += dat * pattern[math.floor((x + 1) / (i + 1)) % len(pattern) ]
                                   
        data[i] = int(str(total)[-1])

for i in range(outputOffset, outputOffset + 9):
    print(data[i])
