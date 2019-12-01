from math import *

f = open("input.txt", "r")

content = f.readlines()

total = 0

for i in range(0, len(content)):
    number = int(content[i])

    number = floor(number / 3)
    number -= 2

    total += number

print(total)
