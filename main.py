import sys
import pygame
import os

from pygame.locals import *
from grid import *


def main():
    # init
    pygame.init()
    dimImage = (707, 1000)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (550, 50)
    display = pygame.display.set_mode(dimImage, 0, 32)
    img = pygame.image.load('Images/full_map_3.png')
    imgBarbarian = pygame.image.load('Images/cube_black.png')
    resizedImg = pygame.transform.scale(img, dimImage)
    display.blit(resizedImg, (0, 0))
    pygame.display.flip()
    colorWhite = (255, 255, 255)
    colorRed = (255, 0, 0)
    colorBlue = (0, 0, 255)
    listPoints = create_grid()

    for point in listPoints:
        pygame.draw.polygon(display, colorWhite, point, 2)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 45 < pos[0] < 741 and 45 < pos[1] < 955:
                    listPoints, hexCliqued, hexToColored = search_hexagon(pos)
                    display.blit(resizedImg, (0, 0))
                    for point in listPoints:
                        if listPoints.index(point) == hexCliqued:
                            pygame.draw.polygon(display, colorRed, point, 0)
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
        pygame.display.update()


main()
