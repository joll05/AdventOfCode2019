import computer

output = ""
total = 0

x = 0
y = 0

def RecieveOutput(out):
    global output
    global total
    
    if(out == 0):
        output += "."
        return
    if(out == 1):
        output += "#"
        total += 1
        return

inputIndex = 0
def SendInput():
    global inputIndex
    inputIndex += 1
    if(inputIndex % 2 == 1):
        return x
    else:
        return y

for X in range(200):
    for Y in range(200):
        x = X
        y = Y
        computer.Run(RecieveOutput, SendInput)

    output += "\n"

print(output)
print(total)
