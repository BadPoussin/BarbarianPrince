import sys
import pygame
import os

from pygame.locals import *
from grid import *


def main():
    # init
    pygame.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (550, 50)
    display = pygame.display.set_mode((787, 1000), 0, 32)
    img = pygame.image.load('Images/full_map_2.png')
    resizedImg = pygame.transform.scale(img, (787, 1000))
    display.blit(resizedImg, (0, 0))
    pygame.display.flip()
    color = (255, 255, 255)
    listPoints = create_grid()

    for list in listPoints:
        pygame.draw.polygon(display, color, list, 2)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()
