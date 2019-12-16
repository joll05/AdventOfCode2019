import computer, pygame, sys
pygame.init()

size = width, height = (800, 800)

spriteSpacing = 16

screen = pygame.display.set_mode(size, pygame.RESIZABLE)

def QuitCheck(eventType):
    if(eventType == pygame.QUIT):
        pygame.display.quit()
        sys.exit()

def RecieveOutput(out):
    pass

direction = 1
def SendInput():
    global direction
    
    while True:
        for event in pygame.event.get()
            QuitCheck(event.type)
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_w): direction = 1
                elif(event.key == pygame.K_s): direction = 2
                elif(event.key == pygame.K_a): direction = 3
                elif(event.key == pygame.K_d): direction = 4

                return direction

position = [0, 0]
def RecieveOutput(out):
    


