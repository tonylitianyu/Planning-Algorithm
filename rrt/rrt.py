
import random
import math

class RRT:
    def __init__(self,domain,origin,delta):
        self.domain = domain
        self.origin = origin
        self.delta = delta
        self.nodes = []
        self.nodes.append(origin)


    def getRandomPoint(self):
        dx = random.randint(0,self.domain[0])
        dy = random.randint(0,self.domain[1])

        D = [dx,dy]
        return D
    
    def findNearestVertex(self, q_rand):
        min_dis = self.domain[0] * 2
        min_node = {}
        for i in self.nodes:
            curr_dis = self.getDistance(q_rand,i["curr"])
            
            if curr_dis < min_dis:
                min_dis = curr_dis
                min_node = i
        return min_node


    def getDistance(self,a,b):
        return math.sqrt(((a[0]-b[0])**2)+((a[1]-b[1])**2))


    def calculateNewVertex(self,min_node, q_rand):
        min_dis = self.getDistance(q_rand,min_node["curr"])
        if min_dis < 0.01:
            q_new = {"curr":min_node["curr"], "parent":min_node}
            return q_new


        ratio = self.delta/min_dis
        x = round(-(min_node["curr"][0]-q_rand[0])*ratio)
        y = round(-(min_node["curr"][1]-q_rand[1])*ratio)

        q_new = {"curr":[min_node["curr"][0]+x, min_node["curr"][1]+y], "parent":min_node}
        return q_new


    




