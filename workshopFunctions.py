import pygame

# drawing functions
def drawCircle(screen, colour, positionX, positionY, radius):
    pygame.draw.circle(screen, colour, [positionX, positionY], radius)
    return 1


def drawCross(screen, colour, positionX, positionY, sideLength, lineWidth):
    pygame.draw.line(screen, colour, [positionX - sideLength/2, positionY - sideLength/2], [positionX + sideLength/2, positionY + sideLength/2], lineWidth)
    pygame.draw.line(screen, colour, [positionX + sideLength/2, positionY - sideLength/2], [positionX - sideLength/2, positionY + sideLength/2], lineWidth)


def drawGrid(screen, colour, winSize, horizontalLines, verticalLines, lineWidth):
    for i in range(verticalLines + 1):
        pygame.draw.line(screen, colour, [i * winSize/(verticalLines+1) - lineWidth/2, 0], [i * winSize/(verticalLines+1) - lineWidth/2, winSize], lineWidth)
    for i in range(horizontalLines + 1):
        pygame.draw.line(screen, colour, [0, i * winSize/(horizontalLines+1) - lineWidth/2], [winSize, i * winSize/(horizontalLines+1) - lineWidth/2], lineWidth)


def drawEndScreen(screen, text, bgColour, winSize):
        pygame.draw.rect(screen, bgColour, pygame.Rect((winSize-text.get_rect().width)/2,(winSize-text.get_rect().height)/2, text.get_rect().width, text.get_rect().height))
        screen.blit(text, [(winSize-text.get_rect().width)/2,(winSize-text.get_rect().height)/2])


# game logic help functions
def createEndScreenText(text, colour):
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 60)
    return font.render(text, False, colour)


def noMoreSpace(field):
    for line in field:
        for column in line:
            if column is 0:
                return False
    return True    

def foreachField(field, func):
    for line in range(len(field)):
        for column in range(len(field[line])):
            func(field[line][column], line, column)

# testing function
def printField(field):
    for line in field:
        print(line)