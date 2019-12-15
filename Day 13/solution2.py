import computer, pygame, time
pygame.init()

resizefactor = 20

ballX = 0
paddleX = 0

def Draw(screen, x, y, tileid):
    if(tileid == 0):
        screen.fill(pygame.Color(0, 0, 100), pygame.Rect(x * resizefactor, y * resizefactor, resizefactor, resizefactor))
    elif(tileid == 1):
        screen.fill(pygame.Color(150, 150, 150), pygame.Rect(x * resizefactor, y * resizefactor, resizefactor, resizefactor))
    elif(tileid == 2):
        screen.fill(pygame.Color(255, 255, 255), pygame.Rect(x * resizefactor, y * resizefactor, resizefactor, resizefactor))
    elif(tileid == 3):
        screen.fill(pygame.Color(0, 255, 150), pygame.Rect(x * resizefactor, y * resizefactor, resizefactor, resizefactor))
        global paddleX
        paddleX = x
    elif(tileid == 4):
        screen.fill(pygame.Color(0, 0, 255), pygame.Rect(x * resizefactor, y * resizefactor, resizefactor, resizefactor))
        global ballX
        ballX = x
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
        if(xPos == -1 and yPos == 0):
            pygame.display.set_caption(str(out))
        Draw(screen, xPos, yPos, out)

    index += 1
    
def SendInput():
    time.sleep(1 / 60)
    pygame.event.get()

    out = 0
    
    if(paddleX > ballX):
        out = -1
    elif(paddleX < ballX):
        out = 1
    
    return out

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

def QuitCheck():
    while True:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.display.quit()

screen = pygame.display.set_mode((size[0] * resizefactor + resizefactor, size[1] * resizefactor + resizefactor))

xPos = 0
yPos = 0
index = 0

computer.Run(RecieveOutput, SendInput, [[0, 2]])

QuitCheck()
