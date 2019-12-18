import math

f = open("input.txt", "r")

data = []

pattern = [0, 1, 0, -1]

for char in f.read():
    data += [int(char)]

for loop in range(100):
    for i in range(len(data)):
        total = 0
        for x, dat in enumerate(data):
            total += dat * pattern[math.floor((x + 1) / (i + 1)) % len(pattern) ]
                                   
        data[i] = int(str(total)[-1])

    print(data)
    if(data == originalData):
        break
