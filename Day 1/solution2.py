from math import *

f = open("input.txt", "r")

content = f.readlines()

total = 0

for i in range(0, len(content)):
    number = int(content[i])

    while True:
        number = floor(number / 3)
        number -= 2

        if(number <= 0):
            break

        total += number

print(total)
