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

#testing to find the cheapest node
cheapest = 0;
for i in range(100):
    if(phoneArr[i].cost < phoneArr[cheapest.cost]):
        cheapest = i;
graph.add_artist(plt.Circle((phoneArr[cheapest].xpos, phoneArr[cheapest].ypos), phoneArr[cheapest].range, color = "green", fill = False))

#size of graph
plt.xlim([0,1000])
plt.ylim([0,1000])
plt.show()