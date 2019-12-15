import computer, pygame
pygame.init()

def Draw(screen, x, y, tileid):
    if(tileid == 0):
        screen.fill(pygame.Color(0, 0, 100), pygame.Rect(x * 10, y * 10, 10, 10))
    elif(tileid == 1):
        screen.fill(pygame.Color(150, 150, 150), pygame.Rect(x * 10, y * 10, 10, 10))
    elif(tileid == 2):
        screen.fill(pygame.Color(255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10))
    elif(tileid == 3):
        screen.fill(pygame.Color(0, 255, 150), pygame.Rect(x * 10, y * 10, 10, 10))
    elif(tileid == 4):
        screen.fill(pygame.Color(0, 0, 255), pygame.Rect(x * 10, y * 10, 10, 10))

    pygame.display.flip()

screen = None

index = 0
xPos = 0
yPos = 0
def RecieveOutput(out):
    global index

    if(index % 3 == 0):
        global xPos
        xPos = out
    elif(index % 3 == 1):
        global yPos
        yPos = out
    else:
        Draw(screen, xPos, yPos, out)

    index += 1

size = width, height = 0, 0
def TestSize(out):
    global index
    global size

    if(index % 3 == 0):
        global xPos
        xPos = out
    elif(index % 3 == 1):
        global yPos
        yPos = out
        if(xPos > size[0] or yPos > size[1]):
            size = width, height = xPos, yPos

    index += 1

computer.Run(TestSize)

screen = pygame.display.set_mode((size[0] * 10 + 10, size[1] * 10 + 10))

xPos = 0
yPos = 0
index = 0

computer.Run(RecieveOutput)

while True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.display.quit()
