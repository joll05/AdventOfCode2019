import numpy as np
import math

f = open("input.txt", "r")

imagedata = f.read()

width = 25
height = 6
layercount = math.ceil(len(imagedata) / (width * height))

image = np.full([width, height], 2, dtype=int)

white = u"\u25A1"
black = u"\u25A0"

for l in range(layercount):
    
    for y in range(height):
        for x in range(width):
            if(image[x, y] != 2):
                continue
            
            currentpos = l * height * width + y * width + x
            num = int(imagedata[currentpos])
            
            image[x, y] = num

# Print it
out = ""
for y in range(height):       
    for x in range(width):
        if(image[x, y] == 0):
            out += black
        else:
            out += white
    out += "\n"

print(out)
