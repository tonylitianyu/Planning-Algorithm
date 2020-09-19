
import sys
import pygame
from a_star.visual import Grid #visualization grid
from a_star.find_path import A_Star
from a_star.maze import Maze #maze obstacle

n_block = 40
origin = [0,0]
target = [n_block-3, n_block-5]
#obstacle = [[2,3],[3,3],[4,3],[5,3],[6,3],[7,3],[8,3]]
finalPath = []



maze = Maze(n_block=n_block,origin=origin,target=target)
obstacle = maze.createObstacle()


grids_visual = Grid(windowSize=400,n_block=n_block, origin=origin, target=target, obstacle=obstacle)
agent = A_Star(origin=origin, target=target, n_block=n_block, obstacle=obstacle)

pygame.time.wait(2000)
while True:
    grids_visual.drawGrid()
    done,result,visited = agent.nextStep()
    
    grids_visual.drawVisited(visited)

    if done:
        finalPath = result
    grids_visual.drawPath(finalPath)

    pygame.time.wait(10)

 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
