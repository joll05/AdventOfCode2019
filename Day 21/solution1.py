import computer

f = open("program1.txt", "r")

program = f.read()

currentChar = 0
def SendInput():
    global currentChar
    result = ord(program[currentChar])
    currentChar += 1
    return result

totalDamage = 0

def RecieveOutput(out):
    if(out < 128):
        # It's an ASCII code
        print(chr(out), end="")
    else:
        # It's a damage number
        global totalDamage
        totalDamage += out

computer.Run(RecieveOutput, SendInput)

print("Total damage: %d" % totalDamage)
