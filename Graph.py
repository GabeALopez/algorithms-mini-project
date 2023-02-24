from createNodes import Phone
from createNodes import phoneSet
from createNodes import neighborhood
from createNodes import purchaseSet
import matplotlib.pyplot as plt
import numpy as np
import random

fig, graph = plt.subplots()

#plots points of Nodes
for i in range(len(phoneSet)):
    graph.scatter(list(phoneSet)[i].xpos, list(phoneSet)[i].ypos, 100, c="black", alpha=0.5, marker=r'$\cdot$',label="Phone")
    
#test circles
graph.add_artist(plt.Circle((neighborhood[0].xpos, neighborhood[0].ypos), 100, color = "red", fill = False))
graph.add_artist(plt.Circle((neighborhood[1].xpos, neighborhood[1].ypos), 100, color = "yellow", fill = False))
graph.add_artist(plt.Circle((neighborhood[2].xpos, neighborhood[2].ypos), 100, color = "orange", fill = False))
graph.add_artist(plt.Circle((neighborhood[3].xpos, neighborhood[3].ypos), 100, color = "blue", fill = False))

for i in range(len(purchaseSet)):
    graph.add_artist(plt.Circle((list(purchaseSet)[i].xpos, list(purchaseSet)[i].ypos), list(purchaseSet)[i].range, color = "green", fill = False))


#size of graph
plt.xlim([0,1000])
plt.ylim([0,1000])
plt.show()