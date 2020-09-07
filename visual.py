import sys
import pygame



class Grid:
    def __init__(self,windowSize,n_block,origin,target,obstacle):
        self.n_block = n_block
        self.windowSize = windowSize
        pygame.init()
        self.SCREEN = pygame.display.set_mode((self.windowSize,self.windowSize))
        self.SCREEN.fill((0,0,0))

        self.origin = origin
        self.target = target
        self.obstacle = obstacle

        self.gridArray = []
        self.fillGridArray()

        self.visited = []


    def fillGridArray(self):
        for i in range(self.n_block):
            self.gridArray.append([])
            for j in range(self.n_block):
                self.gridArray[i].append(0)



        # grid representation using integer array
        # 0 - unvisit, empty
        # 1 - origin
        # 2 - target
        # 3 - obstacle
        # 4 - final path
        # 5 - visited

        # for i in range(self.n_block):
        #     for j in range(self.n_block):
        #         if i == self.origin[0] and j == self.origin[1]:
        #             #assign origin
        #             self.gridArray[i][j] = 1

        #         elif i == self.target[0] and j == self.target[1]:
        #             #assign target end point
        #             self.gridArray[i][j] = 2
        #         else:
        #             self.gridArray[i][j] = 0

        self.gridArray[self.origin[0]][self.origin[1]] = 1
        self.gridArray[self.target[0]][self.target[1]] = 2
        for i in range(len(self.obstacle)):
            self.gridArray[self.obstacle[i][0]][self.obstacle[i][1]] = 3


    def drawGrid(self):
        
        blockSize = int(self.windowSize/self.n_block)
        for i in range(self.n_block):
            for j in range(self.n_block):
                rect = pygame.Rect(i*blockSize,j*blockSize,blockSize,blockSize)
                

                if self.gridArray[i][j] == 1:
                    #draw origin
                    pygame.draw.rect(self.SCREEN,(0,0,255),rect,0)

                elif self.gridArray[i][j] == 2:
                    #draw target end point
                    pygame.draw.rect(self.SCREEN,(255,165,0),rect,0)

                elif self.gridArray[i][j] == 3:
                    pygame.draw.rect(self.SCREEN,(120,120,120),rect,0)
                    
                elif self.gridArray[i][j] == 4:
                    pygame.draw.rect(self.SCREEN,(255,0,0),rect,0)

                elif self.gridArray[i][j] == 5:
                    pygame.draw.rect(self.SCREEN,(0,255,0),rect,0)

                
                pygame.draw.rect(self.SCREEN,(200,200,200),rect,1)

                

    def drawPath(self,path):
        for i in range(len(path)):
            
            waypoint = path[i]
            self.gridArray[waypoint[0]][waypoint[1]] = 4

    def drawVisited(self,visited):
        for i in range(len(visited)):
            visitedBlock = visited[i]
            if visitedBlock == self.origin or visitedBlock == self.target:
                continue
            self.gridArray[visitedBlock[0]][visitedBlock[1]] = 5




        