import sys
import pygame
from workshopFunctions import drawCircle, drawCross, drawGrid, drawEndScreen, foreachField, printField, createEndScreenText, noMoreSpace


###################
#### Variables ####
###################

# Colours
black = 0, 0, 0
grey = 122, 122, 122
white = 255, 255, 255

# window
size = 600
window = None

# game logic

field = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

status = 'playing'
endScreenText = None
turn = 'Player1'

###################
#### Functions ####
###################

# handle mouse clicks
def onClick(cursorPositionX, cursorPositionY):
    global status
    global size
    global field
    global turn
    global endScreenText
    if status == 'playing':
        line = int(3*cursorPositionY/size)
        column = int(3*cursorPositionX/size)
        if turn == 'Player1' and field[line][column] == 0:
            field[line][column] = 1
            turn = 'Player2'
        elif turn == 'Player2' and field[line][column] == 0:
            field[line][column] = 2
            turn = 'Player1'
        if (field[0][0] == field[0][1] == field[0][2] != 0 or field[1][0] == field[1][1] == field[1][2] != 0 or field[2][0] == field[2][1] == field[2][2] != 0 or
            field[0][0] == field[1][0] == field[2][0] != 0 or field[0][1] == field[1][1] == field[2][1] != 0 or field[0][2] == field[1][2] == field[2][2] != 0 or
            field[0][0] == field[1][1] == field[2][2] != 0 or field[0][2] == field[1][1] == field[2][0] != 0):
            status = 'end'
            if turn == 'Player1':
                endScreenText = createEndScreenText('Player 2 won', white)
            else:
                endScreenText = createEndScreenText('Player 1 won', white)
        if noMoreSpace(field) == True:
            status = 'end'
            endScreenText = createEndScreenText('Draw', white)


def drawField(value, line, column):
    global window
    global size
    global white
    if value == 1:
        drawCircle(window, white, size/6 + column *size/3, size/6 + line *size/3, 75)
    elif value == 2:
        drawCross(window, white, size/6 + column *size/3, size/6 + line *size/3, 75, 5)


# handle whats visible in the window
def draw(window):
    global size
    global field
    global white
    global grey
    global status
    global endScreenText
    drawGrid(window, white, size, 2, 2, 5)
    foreachField(field, drawField)
    if status == 'end':
        drawEndScreen(window, endScreenText, grey, size)


#########################
# background game logic #
#     Can be ignored    #
#########################

pygame.init()
window = pygame.display.set_mode([size, size])

while (1):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                onClick(event.pos[0], event.pos[1])
    window.fill(black)
    draw(window)
    pygame.display.flip()
