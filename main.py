
import sys
import pygame
from visual import Grid
from a_star import A_Star

n_block = 40
origin = [0,0]
target = [n_block-3, n_block-5]

grids = Grid(windowSize=400,n_block=n_block, origin=origin, target=target)
agent = A_Star(origin=origin, target=target, n_block=n_block)


while True:
    grids.drawGrid()
    done,result = agent.nextStep()
    if done:
        print(result)
        grids.drawPath(result)

 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
