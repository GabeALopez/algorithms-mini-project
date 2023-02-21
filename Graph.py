from MiniProject1 import Node
from MiniProject1 import phoneArr
import matplotlib.pyplot as plt
import numpy as np
import random

fig, graph = plt.subplots()

#plots points of Nodes
for i in range(100):
    graph.scatter(phoneArr[i].xpos, phoneArr[i].ypos, 100, c="black", alpha=0.5, marker=r'$\cdot$',label="Phone")
    
#test circles
graph.add_artist(plt.Circle((phoneArr[10].xpos, phoneArr[10].ypos), phoneArr[20].range, color = "red", fill = False))
graph.add_artist(plt.Circle((phoneArr[20].xpos, phoneArr[20].ypos), phoneArr[20].range, color = "blue", fill = False))

#size of graph
plt.xlim([0,1000])
plt.ylim([0,1000])
plt.show()