"""
budget = 10
while budget > 0:
    cheapest = 0 #temp
    #loop through and find the cheapest node that is enabled
    for i in range(100):
        if(phoneArr[i].cost < phoneArr[cheapest].cost) & (phoneArr[i].visited):
            cheapest = i;
    
    phoneArr[cheapest].visited = False
    
    if (budget - phoneArr[cheapest].cost < 0):
        break
    else:
        budget = budget - phoneArr[cheapest].cost
    #make circle
    graph.add_artist(plt.Circle((phoneArr[cheapest].xpos, phoneArr[cheapest].ypos), phoneArr[cheapest].range, color = "black", fill = False))
"""
#
#

# Completly Random Algorithm
#
"""
budget = 10
while budget > 0:
    rn = random.randint(0,99)
    if (phoneArr[rn].visited) & (phoneArr[rn].cost < budget):
        graph.add_artist(plt.Circle((phoneArr[cheapest].xpos, phoneArr[cheapest].ypos), phoneArr[cheapest].range, color = "pink", fill = False))
        budget - budget - phoneArr[rn].cost
"""