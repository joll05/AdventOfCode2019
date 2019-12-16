import computer, pygame, sys
pygame.init()

size = width, height = (800, 800)

spriteSpacing = 32

screen = pygame.display.set_mode(size, pygame.RESIZABLE)    

def QuitCheck(eventType):
    if(eventType == pygame.QUIT):
        pygame.display.quit()
        sys.exit()

position = [0, 0]
direction = 1
def SendInput():
    global direction
    
    while True:
        for event in pygame.event.get():
            QuitCheck(event.type)
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_w): direction = 1
                elif(event.key == pygame.K_s): direction = 2
                elif(event.key == pygame.K_a): direction = 3
                elif(event.key == pygame.K_d): direction = 4

                return direction

def GetTargetPosition():
    currentPosition = position
    if(direction == 1): currentPosition[1] += 1
    elif(direction == 2): currentPosition[1] -= 1
    elif(direction == 3): currentPosition[0] += 1
    elif(direction == 4): currentPosition[0] -= 1

    return currentPosition
    
walls = [[]]
systemFound = False
systemLocation = [0, 0]

wall = pygame.image.load("Bricks.png")
robot = pygame.image.load("RepairRobot.png")
def Draw():
    screen.fill(pygame.Color(0, 0, 0))
    print(walls)
    for w in walls:
        objRect = pygame.Rect(w[0] * spriteSpacing, w[1] * spriteSpacing, spriteSpacing, spriteSpacing)
        screen.blit(wall, objRect)

    if(systemFound):
        objRect = pygame.Rect(systemLocation[0] * spriteSpacing, systemLocation[1] * spriteSpacing, spriteSpacing, spriteSpacing)
        screen.fill(pygame.color(0, 255, 0), objRect)

    robotRect = pygame.Rect(position[0] * spriteSpacing, position[1] * spriteSpacing, spriteSpacing, spriteSpacing)
    screen.blit(robot, robotRect)

    pygame.display.flip()
    
def RecieveOutput(out):
    global walls
    global position
    global systemFound
    global systemLocation

    pygame.display.set_caption(str(out))
    
    if(out == 0):
        walls += [GetTargetPosition()]
    elif(out == 1):
        position = GetTargetPosition()
    elif(out == 2):
        position = GetTargetPosition()
        systemFound = True
        systemLocation = position

    Draw()

computer.Run(RecieveOutput, SendInput)
