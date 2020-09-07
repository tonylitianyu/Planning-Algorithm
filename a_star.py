from queue import PriorityQueue
import math


class A_Star:
    def __init__(self,origin,target,n_block):
        self.origin = origin
        self.target = target
        self.n_block = n_block

        self.openSet = PriorityQueue()
        self.openSet.put((0,self.origin))



        self.cameFrom = [[[None,None] for x in range(self.n_block)] for y in range(self.n_block)] 
        

        self.gScore = [[3*self.n_block for x in range(self.n_block)] for y in range(self.n_block)] 
        self.gScore[self.origin[0]][self.origin[1]] = 0


        self.fScore = [[3*self.n_block for x in range(self.n_block)] for y in range(self.n_block)] 
        self.fScore[self.origin[0]][self.origin[1]] = self.getHScore(self.origin)
    
    def reconstruct(self):

        print("start path reconstruction")
        self.openSet.queue.clear()
        totalPath = [self.target]
        current = self.target
        print(current)
        while current[0] != self.origin[0] or current[1] != self.origin[1]:
            
            current = self.cameFrom[current[0]][current[1]]
            totalPath.append(current)
        return totalPath
    

    def getHScore(self, current):
        return math.sqrt((current[0]-self.target[0])**2 + (current[1]-self.target[1])**2)

    def nextStep(self):
        if self.openSet.empty() == True:
            #print("openSet is empty")
            return False, []

        current = self.openSet.get()[1]
        #print(current)
        if current == self.target:
            finalResult = self.reconstruct()
            
            return True, finalResult

        
        currentNeighbor = self.getNeighbor(current)

        for neighbor in currentNeighbor:
            temp_g = self.gScore[current[0]][current[1]]+1

            
            if temp_g < self.gScore[neighbor[0]][neighbor[1]]:
                #came from
                
                

                self.cameFrom[neighbor[0]][neighbor[1]] = current

                self.gScore[neighbor[0]][neighbor[1]] = temp_g
                self.fScore[neighbor[0]][neighbor[1]] = temp_g + self.getHScore(neighbor)

                #print(list(self.openSet.queue))

                enterOpenset = self.neightExistInOpenSet(neighbor,self.openSet)
                

                if enterOpenset is False:
                    
                    self.openSet.put((self.fScore[neighbor[0]][neighbor[1]],neighbor))


        return False, []



    def getNeighbor(self,current):
        neighbor = []

        if current[0] != 0:
            #left neighbor
            neighbor.append([current[0]-1,current[1]])

        if current[1] != 0:
            #up neighbor
            neighbor.append([current[0],current[1]-1])

        if current[0] != (self.n_block-1):
            #right neighbor
            neighbor.append([current[0]+1,current[1]])

        if current[1] != (self.n_block-1):
            #down neighbor
            neighbor.append([current[0],current[1]+1])

        return neighbor

    def neightExistInOpenSet(self,neighbor,pq):
        pq_size = pq.qsize()
        for _ in range(pq_size):
            temp = pq.get()
            
            temp_coor = temp[1]
            pq.put((temp[0],temp_coor))
            if temp_coor[0] == neighbor[0] and temp_coor[1] == neighbor[1]:
                return True

            

        return False



