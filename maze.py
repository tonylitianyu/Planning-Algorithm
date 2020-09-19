import random

# grid representation using integer array
# 0 - unvisit, empty
# 1 - origin
# 2 - target
# 3 - obstacle
# 4 - final path
# 5 - visited



class Maze:
    def __init__(self,n_block,origin,target):
        self.n_block = n_block
        self.origin = origin
        self.target = target
        self.frontier = []
        self.cells = []

        for i in range(self.n_block):
            self.cells.append([])
            for j in range(self.n_block):
                self.cells[i].append(3)

    def createObstacle(self):

        # All cells are walls.
        # Randomly choose a cell B and mark it as free. 
        # Add that cell's neighbors to the frontier list.
        # While the frontier list is not empty:
        #     Randomly choose a wall C from the frontier list
        #     Let F be a randomly chosen nearest two hop empty cell of C
        #     Remove the wall between C and F
        #     Make C free
        #     Add two hop neighbor of C to the frontier list
        #     Remove C from the wall list
        
        Bx = random.randint(0,self.n_block-1)
        By = random.randint(0,self.n_block-1)
        B = [Bx,By]
        
        self.cells[Bx][By] = 0
        self.addTwoHopNeighborWall(B)
        

        while len(self.frontier) > 0:
            C = random.choice(self.frontier)
            self.connectNearestEmpty(C)
            self.cells[C[0]][C[1]] = 0
            self.addTwoHopNeighborWall(C)
            self.frontier.remove(C)

        self.cells[self.origin[0]][self.origin[1]] = 0
        self.cells[self.target[0]][self.target[1]] = 0
        obstacles = self.generateObstacleList()
        return obstacles



    def addTwoHopNeighborWall(self,cell):
        #x+1,x-1,y+1,y-1
        
        x = cell[0]
        y = cell[1]

        if (x-1 > 0) and ([x-2,y] not in self.frontier) and (self.cells[x-2][y] == 3):
            self.frontier.append([x-2,y])

        if (y-1 > 0) and ([x,y-2] not in self.frontier) and (self.cells[x][y-2] == 3):
            self.frontier.append([x,y-2])

        if (x+1 < self.n_block-1) and ([x+2,y] not in self.frontier) and (self.cells[x+2][y] == 3):
            self.frontier.append([x+2,y])

        if (y+1 < self.n_block-1) and ([x,y+2] not in self.frontier) and (self.cells[x][y+2] == 3):
            self.frontier.append([x,y+2])


    def connectNearestEmpty(self,cell):
        result = []
        x = cell[0]
        y = cell[1]

        if (x-1 > 0) and self.cells[x-2][y] == 0:
            result.append([x-2,y])

        if (y-1 > 0) and self.cells[x][y-2] == 0:
            result.append([x,y-2])

        if (x+1 < self.n_block-1) and self.cells[x+2][y] == 0:
            result.append([x+2,y])

        if (y+1 < self.n_block-1) and self.cells[x][y+2] == 0:
            result.append([x,y+2])


        F = random.choice(result)
        self.cells[int(abs((x+F[0])/2))][int(abs((y+F[1])/2))] = 0

    def generateObstacleList(self):
        obstacles = []
        for i in range(self.n_block):
            for j in range(self.n_block):
                if self.cells[i][j] == 3:
                    obstacles.append([i,j])

        return obstacles
        