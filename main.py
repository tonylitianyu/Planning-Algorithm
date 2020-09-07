
import sys
import pygame
from visual import Grid
from a_star import A_Star

n_block = 10
origin = [0,0]
target = [n_block-3, n_block-5]
obstacle = [[2,3],[3,3],[4,3],[5,3],[6,3],[7,3],[8,3]]
finalPath = []


grids = Grid(windowSize=400,n_block=n_block, origin=origin, target=target, obstacle=obstacle)
agent = A_Star(origin=origin, target=target, n_block=n_block, obstacle=obstacle)

pygame.time.wait(5000)
while True:
    grids.drawGrid()
    done,result,visited = agent.nextStep()
    
    grids.drawVisited(visited)

    if done:
        finalPath = result
    grids.drawPath(finalPath)

    pygame.time.wait(100)

 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
