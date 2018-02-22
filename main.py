import sys
import pygame
import os

from pygame.locals import *
from game import *
from grid import *


def main():
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
    listColored = []

    clear = lambda: os.system('cls')
    clear()

    diceNumber = roll_dice()
    imgDice = pygame.image.load('Images/dice' + str(diceNumber) + '.png')
    display.blit(imgDice, (70, 880))

    depart, cote, xDepart, listColored = start_position(1, listColored)
    oldHex = depart

    for point in listPoints:
        if listPoints.index(point) == depart:
            pygame.draw.polygon(display, colorRed, point, 0)
        elif listPoints.index(point) in cote:
            pygame.draw.polygon(display, colorBlue, point, 2)
        else:
            pygame.draw.polygon(display, colorWhite, point, 2)

    display.blit(imgBarbarian, (xDepart, 85))

    barbName = input("Saisissez le nom de votre prince barbare : ")
    print("Votre nom est donc " + str(barbName) + ".")

    life = 100
    tour = 1
    combat_skill = 8
    endurance = 9
    wealth_code = 2
    wit = 2

    print("Vous commencez la partie. Début du tour 1.")
    print()
    print("Vous êtes sur la case en position de départ n°" + str(diceNumber))
    print()
    display_carac(life, combat_skill, endurance, wealth_code, wit, "")

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
                        isRoadTaken = road_taken(oldHex, hexCliqued)
                        oldHex = hexCliqued
                        tour = next_tour(tour)
                        display_carac(combat_skill, endurance, wealth_code, wit, diceNumber)
                        if not isRoadTaken:
                            display.blit(imgDice, (70, 880))
                            launch_event(diceNumber, hexCliqued)
                        if win_game(wealth_code):
                            print("Vous avez gagné la partie, félicitations !")
        pygame.display.update()


main()
