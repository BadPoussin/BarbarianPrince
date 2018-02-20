import sys
import pygame
import os

from pygame.locals import *
from game import *
from grid import *


def main():
    # init
    pygame.init()
    dimImage = (707, 1000)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 50)
    display = pygame.display.set_mode(dimImage, 0, 32)
    img = pygame.image.load('Images/full_map_3.png')
    imgBarbarian = pygame.image.load('Images/barbarian.png')
    resizedImg = pygame.transform.scale(img, dimImage)
    display.blit(resizedImg, (0, 0))
    pygame.display.flip()
    colorWhite = (255, 255, 255)
    colorRed = (255, 0, 0)
    colorBlue = (0, 0, 255)
    listPoints = create_grid()
    listColored = [0, 1, 20]

    for point in listPoints:
        if listPoints.index(point) == 0:
            pygame.draw.polygon(display, colorRed, point, 0)
        elif listPoints.index(point) == 1 or listPoints.index(point) == 20:
            pygame.draw.polygon(display, colorBlue, point, 2)
        else:
            pygame.draw.polygon(display, colorWhite, point, 2)

    display.blit(imgBarbarian, (65, 85))

    clear = lambda: os.system('cls')
    clear()

    tour = 1
    combat_skill = 8
    endurance = 9
    wealth_code = 2
    wit = 10

    print("Vous commencez la partie. Début du tour 1.")
    display_carac(combat_skill, endurance, wealth_code, wit, "")

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                diceNumber = str(roll_dice())
                imgDice = pygame.image.load('Images/dice' + diceNumber + '.png')
                listPoints, hexCliqued, hexCenter, hexToColored = search_hexagon(pos)
                if hexCliqued != -1:
                    if hexCliqued in listColored:
                        listColored.clear()
                        display.blit(resizedImg, (0, 0))
                        for point in listPoints:
                            if listPoints.index(point) == hexCliqued:
                                pygame.draw.polygon(display, colorRed, point, 0)
                                display.blit(imgBarbarian, (hexCenter.x - 11.5, hexCenter.y - 12))
                                listColored.append(hexCliqued)
                            else:
                                isColored = False
                                for hex in hexToColored:
                                    if listPoints.index(point) == hex:
                                        isColored = True
                                        break

                                if not isColored:
                                    pygame.draw.polygon(display, colorWhite, point, 2)
                                else:
                                    pygame.draw.polygon(display, colorBlue, point, 2)
                                    listColored.append(listPoints.index(point))
                        tour = next_tour(tour)
                        display_carac(combat_skill, endurance, wealth_code, wit, diceNumber)
                        display.blit(imgDice, (70, 880))
        pygame.display.update()


main()
