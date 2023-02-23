from createNodes import Phone
from createNodes import phoneArr
from createNodes import neighborhood
from createNodes import k
from createNodes import num
import matplotlib.pyplot as plt
import numpy as np
import random

fig, graph = plt.subplots()

#plots points of Phones
for i in range(k):
    graph.scatter(phoneArr[i].xpos, phoneArr[i].ypos, 100, c="black", alpha=0.5, marker=r'$\cdot$',label="Phone")
    
#test circles
graph.add_artist(plt.Circle((neighborhood[0].xpos, neighborhood[0].ypos), 100, color = "red", fill = False))
graph.add_artist(plt.Circle((neighborhood[1].xpos, neighborhood[1].ypos), 100, color = "yellow", fill = False))
graph.add_artist(plt.Circle((neighborhood[2].xpos, neighborhood[2].ypos), 100, color = "orange", fill = False))
graph.add_artist(plt.Circle((neighborhood[3].xpos, neighborhood[3].ypos), 100, color = "blue", fill = False))

#testing greedy
#temp budget
budget = 10
cheapest = 0
while budget > 0:
    for i in range(num):
        if phoneArr[i].visited == False:
            cheapest = i
            break
    print("Budget: ",round(budget, 2))
    #loop through and find the cheapest Phone that is enabled
    for i in range(num):
        if(phoneArr[i].costPerPhone < phoneArr[cheapest].costPerPhone) & (phoneArr[i].visited == False):
            cheapest = i
    if (budget - phoneArr[cheapest].cost < 0):
        break
    else:
        budget = budget - phoneArr[cheapest].cost
        phoneArr[cheapest].visited = True
<<<<<<< Updated upstream
        for i in range(num):
            if phoneArr[cheapest].inRangeArr[i] == True:
                phoneArr[i].visited = True
                for i in range(num):
                    if phoneArr[cheapest].inRangeArr[i] == True:
                        phoneArr[i].numInRange = phoneArr[i].numInRange - 1
                        if phoneArr[i].numInRange > 0:
                            phoneArr[i].costPerNode = round(phoneArr[i].cost / phoneArr[i].numInRange, 2)
                        else:
                            phoneArr[i].costPerNode = phoneArr[i].cost
=======
        for j in range(num):
            if phoneArr[cheapest].inRangeArr[j] == True:
                phoneArr[j].visited = True
                for m in range(num):
                    if phoneArr[cheapest].inRangeArr[m] == True:
                        phoneArr[m].numInRange = phoneArr[m].numInRange - 1
                        if phoneArr[m].numInRange > 0:
                            phoneArr[m].costPerPhone = round(phoneArr[m].cost / phoneArr[m].numInRange + 1, 2)
                        else:
                            phoneArr[m].costPerPhone = phoneArr[m].cost
>>>>>>> Stashed changes

        print("Buy Phone:", cheapest, "cost:", phoneArr[cheapest].cost, "costperPhone:", phoneArr[cheapest].costPerPhone)

    #make circle
        graph.add_artist(plt.Circle((phoneArr[cheapest].xpos, phoneArr[cheapest].ypos), phoneArr[cheapest].range, color = "green", fill = False))
 
    #Then take all Phones in range of this one and disable them

#size of graph
plt.xlim([0,1000])
plt.ylim([0,1000])
plt.show()