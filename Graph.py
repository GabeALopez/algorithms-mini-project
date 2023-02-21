from MiniProject1 import Phone
import matplotlib.pyplot as plt
import numpy as np
import random

arry = [Phone] * 100

fig, graph = plt.subplots()

for i in range(100):
    arry[i].xpos = random.randint(0, 1000)
    arry[i].ypos = random.randint(0, 1000)
    print(arry[i].xpos)
    print(arry[i].ypos)
    graph.scatter(arry[i].xpos, arry[i].ypos, 100, c="black", alpha=0.5, marker=r'$\cdot$',label="Phone")
    

plt.xlim([0,1000])
plt.ylim([0,1000])
plt.show()