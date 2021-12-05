import sys, pygame, random
from pygame.display import update
import time
import colorsys
from sorting_algorithms import *

from pygame.draw import rect

pygame.init()

size = width, height = 2560, 1440
arraySize = 700
array = list(range(1, arraySize+1))
speed = [2, 2]
black = (150,150,150,0)
black = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255),0)
white = (125, 125, 125)
colorStart = random.random()

rectangles = []
rectangleWidth = width / arraySize
heightMultiplier = height / max(array)

screen = pygame.display.set_mode(size)

for i in range(arraySize):
    rectangeHeight = array[i] * heightMultiplier
    rectangles.append(pygame.Rect((i * rectangleWidth), height-rectangeHeight, rectangleWidth, rectangeHeight))

def shuffleArray(array):
     random.shuffle(array)

def randomizeArray(array):
    for i in range(len(array)):
        array[i] = random.randint(1, arraySize)
        if i % 10 == 0:
            drawArray(array)

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

def drawArray(array):
    pygame.event.get()
    screen.fill(black)
    rectangleWidth = width / len(array)
    heightMultiplier = height / max(array)
    startX = 0
    startY = height
    i = 0
    for element, rect in zip(array, rectangles):
        rectangeHeight = element * heightMultiplier
        rect.update((i * rectangleWidth), height-rectangeHeight, rectangleWidth+1, rectangeHeight)
        temp = element/(arraySize*4)+(colorStart)
        if temp > 1:
            temp -= 1
        color = hsv2rgb(temp, 1, 0.6)
        pygame.draw.rect(screen, color, rectangles[i])
        i += 1
    pygame.display.flip()

while True:
    black = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255),0)
    colorStart = random.random()
    randomizeArray(array)
    # shuffleArray(array)
    i = random.randint(0, 9)
    if i == 0:
        bubbleSort(array, drawArray)
    elif i == 1:
        insertionSort(array, drawArray)
    elif i == 2:
        selectionSort(array, drawArray)
    elif i == 3:
        quickSort(array, 0, len(array)-1, drawArray)
    elif i == 4:
        heapSort(array, drawArray)
    elif i == 5:
        mergeSort(array, 0, len(array)-1, drawArray)
    elif i == 6:
        shellSort(array, drawArray)
    elif i == 7:
        pancakeSort(array, len(array), drawArray)
    elif i == 8:
        bucketSort(array, drawArray)
    else:
        bitonicSort(array , 0, len(array), 1, drawArray)


# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()
