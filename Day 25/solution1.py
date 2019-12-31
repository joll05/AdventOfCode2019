import computer

def GetCommand():
    userInput = input()

    return userInput + "\n"

def RecieveOutput(out):
    print(chr(out), end="")

command = ""
def SendInput():
    global command
    if(command == ""):
        command = GetCommand()

    currentChar = command[0]
    command = command[1:]
    return ord(currentChar)

computer.Run(RecieveOutput, SendInput)
