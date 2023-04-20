# Simple pygame program

# Import and initialize the pygame library
import pygame
import ctypes
import time
from random import *
pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
COLOR_BOX = (255, 255, 255)
COLOR_BOX_TRANSPERANCT = (0, 0, 0, 0)
BOX = 35
NUMBER_RESULT = list(map(int, str(randint(1000, 9999))))
print('NUMBER_RESULT', NUMBER_RESULT)

FULL_ARRAY_INPUT_DEFAULT = [[],[],[],[],[],[],[],[],[],[]]
FULL_ARRAY_RESULT_DEFAULT = [[],[],[],[],[],[],[],[],[],[]]
FULL_ARRAY_INPUT = FULL_ARRAY_INPUT_DEFAULT
FULL_ARRAY_RESULT = FULL_ARRAY_RESULT_DEFAULT
CURRENT_INDEX = 0

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Fill the background with white
screen.fill((238, 238, 238))

# Draw sqare for input & result
def drawWrapped():
    TOP_POSITION = 120
    LEFT_POSITION = 30
    for i in range(0,10):
        LEFT_POSITION_ITEM = LEFT_POSITION
        for j in range(0,6):
            pygame.draw.rect(screen, COLOR_BOX, pygame.Rect(LEFT_POSITION_ITEM,TOP_POSITION,BOX,BOX))
            LEFT_POSITION_ITEM += BOX + 20
            if (j == 3):
                LEFT_POSITION_ITEM += 30
        TOP_POSITION += BOX + 10

def calInput(inputP):
    print('Press', inputP)
    if (CURRENT_INDEX < 10 and len(FULL_ARRAY_INPUT[CURRENT_INDEX]) < 4):
        FULL_ARRAY_INPUT[CURRENT_INDEX].append(inputP)

def calEnter():
    global CURRENT_INDEX
    global NUMBER_RESULT
    if (CURRENT_INDEX < 10 and len(FULL_ARRAY_INPUT[CURRENT_INDEX]) == 4):
        FULL_ARRAY_RESULT[CURRENT_INDEX].append(calCorrectNumber(NUMBER_RESULT, FULL_ARRAY_INPUT[CURRENT_INDEX]))
        FULL_ARRAY_RESULT[CURRENT_INDEX].append(calCorrectPosition(NUMBER_RESULT, FULL_ARRAY_INPUT[CURRENT_INDEX]))
        CURRENT_INDEX += 1

def calCorrectNumber(NUMBER_FOR_CHECK, ARRAY_NUMBER):
    CORRECT_NUMBER = 0
    # ARRAY_NUMBER_ALREADY_CHECK = []
    for i in NUMBER_FOR_CHECK:
        # if i in ARRAY_NUMBER and i not in ARRAY_NUMBER_ALREADY_CHECK:
        if i in ARRAY_NUMBER:
            # ARRAY_NUMBER_ALREADY_CHECK.append(i)
            CORRECT_NUMBER += 1
    return CORRECT_NUMBER


def calCorrectPosition(NUMBER_FOR_CHECK, ARRAY_NUMBER):
    CORRECT_POSITION = 0
    for i in range(0,4):
        if NUMBER_FOR_CHECK[i] == ARRAY_NUMBER[i]:
            CORRECT_POSITION += 1
    return CORRECT_POSITION


def calBackSpace():
    global CURRENT_INDEX
    FULL_ARRAY_INPUT[CURRENT_INDEX] = FULL_ARRAY_INPUT[CURRENT_INDEX][:-1]

def drawText(text, topPosition, leftPosition, fz = 10, cl = (255,255,255)):
    font1 = pygame.font.Font('freesansbold.ttf', fz)
    text = font1.render(str(text), True, (0,0,0), cl)
    textRect = text.get_rect()
    textRect.center = (leftPosition,topPosition)
    screen.blit(text, textRect)

green = (0, 255, 0)
blue = (0, 0, 128)
white = (255, 255, 255)
font = pygame.font.Font('freesansbold.ttf', 32)


def drawNumber(text, topPosition, leftPosition):
    text = font.render(str(text), True, green, white)
    textRect = text.get_rect()
    textRect.center = (leftPosition,topPosition)
    screen.blit(text, textRect)

TOP_POSITION_INPUT_DEFAULT = 138
LEFT_POSITION_INPUT_DEFAULT = 47

TOP_POSITION_RESULT_DEFAULT = 138
LEFT_POSITION_RESULT_DEFAULT = 298

def drawListumber():
    TOP_POSITION_INPUT = TOP_POSITION_INPUT_DEFAULT
    for i in range(len(FULL_ARRAY_INPUT)):
        LEFT_POSITION_INPUT = LEFT_POSITION_INPUT_DEFAULT
        for j in range(len(FULL_ARRAY_INPUT[i])):
            drawNumber(FULL_ARRAY_INPUT[i][j], TOP_POSITION_INPUT, LEFT_POSITION_INPUT)
            LEFT_POSITION_INPUT += BOX + 20
            if (j == 3):
                LEFT_POSITION_INPUT += 30
        TOP_POSITION_INPUT += BOX + 10

    
    TOP_POSITION_RESULT = TOP_POSITION_RESULT_DEFAULT
    for i in range(len(FULL_ARRAY_RESULT)):
        LEFT_POSITION_RESULT = LEFT_POSITION_RESULT_DEFAULT
        for j in range(len(FULL_ARRAY_RESULT[i])):
            print(i, j)
            drawNumber(FULL_ARRAY_RESULT[i][j], TOP_POSITION_RESULT, LEFT_POSITION_RESULT)
            LEFT_POSITION_RESULT += BOX + 20
        TOP_POSITION_RESULT += BOX + 10

def checkSuccess():
    if len(FULL_ARRAY_RESULT[CURRENT_INDEX-1]) > 0:
        if FULL_ARRAY_RESULT[CURRENT_INDEX-1][1] == 4:
            return True
        elif (CURRENT_INDEX == 10):
            return False

def retry():
    FULL_ARRAY_RESULT = FULL_ARRAY_RESULT_DEFAULT
    FULL_ARRAY_INPUT =  FULL_ARRAY_INPUT_DEFAULT
    drawWrapped()

drawText('Guess My Number?', 30, 200, 30)

drawText('Your Guess', 88, 125, 18)
drawText('Correct', 80, 300)
drawText('Numbers', 95, 300)
drawText('Correct', 80, 350)
drawText('Positions', 95, 350)

pygame.draw.rect(screen, (200,200,200), pygame.Rect(30,80,20,20))
drawText('?', 91, 40, 16,(200,200,200))

drawWrapped()

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            isSuccess = checkSuccess()
            print('isSuccess', isSuccess)
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_F5:
                retry()
            elif isSuccess == True:
                print('SUCCESS')
                Mbox('SUCCESS', 'Đoán đúng rùi còn định bắt người ta phục vụ nữa hả?????', 1)
            elif isSuccess == False:
                Mbox('HÔ HÔ', 'Chơi lại đi', 1)
            else:
                drawWrapped()
                if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                    calInput(0)
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    calInput(1)
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    calInput(2)
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    calInput(3)
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    calInput(4)
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    calInput(5)
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    calInput(6)
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    calInput(7)
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    calInput(8)
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    calInput(9)
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    calEnter()
                if event.key == pygame.K_BACKSPACE:
                    calBackSpace()

                drawListumber()
                isSuccess = checkSuccess()
                if (isSuccess == True):
                    time.sleep(1)
                    print('SUCCESS')
                    Mbox('SUCCESS', 'Cung hị Cung hị', 1)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()