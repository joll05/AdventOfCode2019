import computer

image = ""

def RecieveOutput(out):
    global image
    image += chr(out)

computer.Run(RecieveOutput)

print(image)
