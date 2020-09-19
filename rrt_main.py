import random
import math
import matplotlib.pyplot as plt
from rrt.rrt import RRT
from rrt.collision import Collision
import imageio
from PIL import Image
import numpy as np

random.seed(6)

im = Image.open('rrt/N_map.png').convert('L')

im = np.flipud(im)

plt.imshow(im, cmap='gray')

D = [im.shape[0],im.shape[1]]
max_step_allow = 5
n_step = 1000

#generate random origin and target
collision = Collision(im)
q_init_curr = collision.getCollisionFreePoint()
q_init = {"curr":q_init_curr,"parent":None}

q_target_curr = collision.getCollisionFreePoint()
q_target = {"curr":q_target_curr,"parent":q_target_curr}


#initialization for agent
rrt_agent = RRT(D,q_init,max_step_allow)

#prepare for plotting
fig = plt.gcf()
fig.show()
fig.canvas.draw()
plt.xlim([0, D[0]])
plt.ylim([0, D[1]])

plt.scatter(q_init_curr[0],q_init_curr[1])
plt.scatter(q_target_curr[0],q_target_curr[1])


while collision.isTargetCollisionFree(rrt_agent.nodes, q_target) == False:

    q_rand = rrt_agent.getRandomPoint() #q_rand is [x,y]
    q_near = rrt_agent.findNearestVertex(q_rand) #q_near is {"curr":[x1,y1], "parent":{}}
    q_new = rrt_agent.calculateNewVertex(q_near, q_rand) #q_new is {"curr":[x1,y1], "parent":{}}

    line_arr = collision.lineOccupation(q_near["curr"],q_new["curr"])
    collision_flag = collision.checkNewPathCollision(line_arr)
    if collision_flag == False:
        
        rrt_agent.nodes.append(q_new)

        plt.plot([q_new["curr"][0],q_new["parent"]["curr"][0]],[q_new["curr"][1],q_new["parent"]["curr"][1]], color='b')
        plt.scatter(q_new["curr"][0],q_new["curr"][1],5,color='b')
        fig.canvas.draw()

print("found target!")

target_parent = rrt_agent.findNearestVertex(q_target_curr)
q_target["parent"] = collision.getLastNode()

curr_node = q_target
while curr_node["parent"] != None:
    plt.plot([curr_node["curr"][0],curr_node["parent"]["curr"][0]],[curr_node["curr"][1],curr_node["parent"]["curr"][1]], color='r')
    curr_node = curr_node["parent"]
    fig.canvas.draw()


plt.show()





