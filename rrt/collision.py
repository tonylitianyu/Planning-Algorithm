


import random
import math
import numpy as np

class Collision:

    def __init__(self,map):
        
        self.map = map
        self.obstacles = []
        self.lastNode = {}

    
    def getCollisionFreePoint(self):
        ox = random.randint(0,len(self.map)-1)
        oy = random.randint(0,len(self.map[0])-1)

        while self.map[oy][ox] == 0:
            
            ox = random.randint(0,len(self.map)-1)
            oy = random.randint(0,len(self.map[0])-1)

        return [ox,oy]


    def __lineLow(self,a,b): #x span > y span
        result = []
        deltax = b[0]-a[0]
        deltay = b[1]-a[1]
        yi = 1
        if deltay < 0:
            yi = -1
            deltay = -deltay

        delta_err = (2*deltay)-deltax
        y = a[1]
        for x in range(a[0],b[0]):
            result.append([x,y])
            if delta_err > 0:
                y = y + yi
                delta_err = delta_err+(2*(deltay-deltax))
            else:
                delta_err = delta_err+(2*deltay)

        return result


    def __lineHigh(self, a, b): # y_span > x_span
        result = []
        deltax = b[0]-a[0]
        deltay = b[1]-a[1]
        xi = 1
        if deltax < 0:
            xi = -1
            deltax = -deltax

        delta_err = (2*deltax)-deltay
        x = a[0]
        for y in range(a[1],b[1]):
            result.append([x,y])
            if delta_err > 0:
                x = x + xi
                delta_err = delta_err+(2*(deltax-deltay))
            else:
                delta_err = delta_err+(2*deltax)

        return result


        

    def lineOccupation(self, a,b):
        if abs(b[1]-a[1]) < abs(b[0]-a[0]):
            if a[0] > b[0]:
                return self.__lineLow(b,a)
            else:
                return self.__lineLow(a,b)
        
        else:
            if a[1] > b[1]:
                return self.__lineHigh(b,a)
            else:
                return self.__lineHigh(a,b)
        


    def checkNewPathCollision(self,line_arr):
        for i in line_arr:
            if self.map[i[1]][i[0]] == 0:
                
                return True

        return False


    def isTargetCollisionFree(self, nodes, target):
        for i in nodes:
            line_arr = self.lineOccupation(i["curr"],target["curr"])
            collision_flag = self.checkNewPathCollision(line_arr)
            if collision_flag == False:
                self.lastNode = i
                return True #find target
        return False

    def getLastNode(self):
        return self.lastNode


    

