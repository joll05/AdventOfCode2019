import math

f = open("input.txt", "r")

imagedata = f.read()

width = 25
height = 6
layercount = math.ceil(len(imagedata) / (width * height))

leastzerocount = width * height + 1
currentresult = 0

for l in range(layercount):
    zerocount = 0
    onecount = 0
    twocount = 0
    
    for x in range(width):
        for y in range(height):
            currentpos = l * width * height + x * height + y
            num = int(imagedata[currentpos])

            if(num == 0):
                zerocount += 1
            elif(num == 1):
                onecount += 1
            elif(num == 2):
                twocount += 1
    if(zerocount < leastzerocount):
        currentresult = onecount * twocount
        leastzerocount = zerocount

print(currentresult)
