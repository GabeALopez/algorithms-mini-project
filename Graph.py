from createNodes import Node
from createNodes import phoneArr
from createNodes import k
import matplotlib.pyplot as plt
import numpy as np
import random

fig, graph = plt.subplots()

#plots points of Nodes
for i in range(k):
    graph.scatter(phoneArr[i].xpos, phoneArr[i].ypos, 100, c="black", alpha=0.5, marker=r'$\cdot$',label="Phone")
    
#test circles
graph.add_artist(plt.Circle((phoneArr[10].xpos, phoneArr[10].ypos), phoneArr[20].range, color = "red", fill = False))
graph.add_artist(plt.Circle((phoneArr[20].xpos, phoneArr[20].ypos), phoneArr[20].range, color = "blue", fill = False))

#testing greedy
#temp budget
budget = 5
while budget > 0:
    cheapest = 0 #temp
    #loop through and find the cheapest node that is enabled
    for i in range(100):
        if(phoneArr[i].cost < phoneArr[cheapest].cost) & (phoneArr[i].enabled):
            cheapest = i;
    
    phoneArr[cheapest].enabled = False
    
    if (budget - phoneArr[cheapest].cost < 0):
        break
    else:
        budget = budget - phoneArr[cheapest].cost
        #test print node
        print("Node cheap", cheapest,": ", "x:", phoneArr[cheapest].xpos, "y:", phoneArr[cheapest].ypos," cost: ",phoneArr[cheapest].cost)
    
    #test print budget
    print("Budget: ",budget)

    #make circle
    graph.add_artist(plt.Circle((phoneArr[cheapest].xpos, phoneArr[cheapest].ypos), phoneArr[cheapest].range, color = "green", fill = False))
    #Then take all nodes in range of this one and disable them


#size of graph
plt.xlim([0,1000])
plt.ylim([0,1000])
plt.show()