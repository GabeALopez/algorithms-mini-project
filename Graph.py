'''
from createNodes import phoneSet
from createNodes import cluster
from createNodes import purchaseSet
import matplotlib.pyplot as plt

fig, graph = plt.subplots()

#plots points of Nodes
#red = (0.1 - 1), orange = (1.1 - 2.5), blue = (2.6 - 4), green = (4.1 - 5.5)
for i in range(len(phoneSet)):
    if list(phoneSet)[i].cost <= 1:
        graph.scatter(list(phoneSet)[i].xpos, list(phoneSet)[i].ypos, 100, c="red", alpha=0.5, marker=r'$\cdot$',label="Phone")
    elif list(phoneSet)[i].cost <= 2.5:
        graph.scatter(list(phoneSet)[i].xpos, list(phoneSet)[i].ypos, 100, c="orange", alpha=0.5, marker=r'$\cdot$',label="Phone")
    elif list(phoneSet)[i].cost <= 4:
        graph.scatter(list(phoneSet)[i].xpos, list(phoneSet)[i].ypos, 100, c="blue", alpha=0.5, marker=r'$\cdot$',label="Phone")
    elif list(phoneSet)[i].cost <= 5.5:
        graph.scatter(list(phoneSet)[i].xpos, list(phoneSet)[i].ypos, 100, c="green", alpha=0.5, marker=r'$\cdot$',label="Phone")
 
#test circles
# graph.add_artist(plt.Circle((cluster[0].xpos, cluster[0].ypos), 100, color = "red", fill = False))
# graph.add_artist(plt.Circle((cluster[1].xpos, cluster[1].ypos), 100, color = "yellow", fill = False))
# graph.add_artist(plt.Circle((cluster[2].xpos, cluster[2].ypos), 100, color = "orange", fill = False))
# graph.add_artist(plt.Circle((cluster[3].xpos, cluster[3].ypos), 100, color = "blue", fill = False))

#draws circles around the purchased phones
for i in range(len(purchaseSet)):
    graph.add_artist(plt.Circle((list(purchaseSet)[i].xpos, list(purchaseSet)[i].ypos), list(purchaseSet)[i].range, color = "green", fill = False))


#size of graph
plt.xlim([0,1000])
plt.ylim([0,1000])
plt.show()
'''