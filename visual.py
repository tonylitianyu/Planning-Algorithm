import sys
import pygame



class Grid:
    def __init__(self,windowSize,n_block,origin,target):
        self.n_block = n_block
        self.windowSize = windowSize
        pygame.init()
        self.SCREEN = pygame.display.set_mode((self.windowSize,self.windowSize))
        self.SCREEN.fill((0,0,0))

        self.origin = origin
        self.target = target

        self.gridArray = []
        self.fillGridArray()


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
        # 4 - visited

        for i in range(self.n_block):
            for j in range(self.n_block):
                if i == self.origin[0] and j == self.origin[1]:
                    #assign origin
                    self.gridArray[i][j] = 1

                elif i == self.target[0] and j == self.target[1]:
                    #assign target end point
                    self.gridArray[i][j] = 2
                else:
                    self.gridArray[i][j] = 0


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
                    pygame.draw.rect(self.SCREEN,(0,255,0),rect,0)

                elif self.gridArray[i][j] == 3:
                    pygame.draw.rect(self.SCREEN,(120,120,120),rect,0)
                    
                elif self.gridArray[i][j] == 4:
                    pygame.draw.rect(self.SCREEN,(255,0,0),rect,0)

                else:
                    pygame.draw.rect(self.SCREEN,(200,200,200),rect,1)

    def drawPath(self,path):
        for i in range(len(path)):
            waypoint = path[i]
            self.gridArray[waypoint[0]][waypoint[1]] = 4




        