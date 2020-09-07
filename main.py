
import sys
import pygame
from visual import Grid



grids = Grid(windowSize=400,n_block=10)


while True:
    grids.drawGrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
