import random
import math 
import numpy as np
import matplotlib.pyplot as plt
        
class Coordinates:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
class Phone(Coordinates):
    def __init__(self,xpos, ypos, cost):
        Coordinates.__init__(self, xpos, ypos)
        self.cost = cost
        self.costPerPhone = 0
        self.range = 50
        self.visited = bool(0)
        self.inRangeSet = set()
        self.numInRange = 0     
    def addPhone(self, phone):
        self.inRangeSet.add(phone)
        self.numInRange = len(self.inRangeSet)
        self.findCPP()
    def removePhone(self, phone):
        self.inRangeSet.discard(phone)
        self.numInRange = len(self.inRangeSet)
        self.findCPP()
    def findCPP(self):
        self.costPerPhone = round(self.cost/(self.numInRange), 2)

np.random.seed(100)
num = 100
budget = 50
#0 = cluster, 1 = distributed
generateType = 0
<<<<<<< HEAD:createNodes.py
algorithmType = 2
=======
algorithmType = 0
>>>>>>> f2a1410d9fff9ac0fa8e898afaf0215578ff8800:Main.py

phoneSet = set()
cluster = [Coordinates] * 4

match generateType:
    #Cluster
    case 0:
        rangeLower = -100
        rangeHigher = 100
        clusterLower = 200
        clusterHigher = 800
    #Randomly Distributed
    case 1:
        rangeLower = -500
        rangeHigher = 500
        clusterLower = 499
        clusterHigher = 500
    #Defaults to cluster
    case _:
        rangeLower = -100
        rangeHigher = 100
        clusterLower = 200
        clusterHigher = 800        
        
#generates phones with different costs and connects them as they generate
#generates first 3 waves costing (0.1 - 1), (1.1 - 2.5), (2.6 - 4) then remaining wave costing (4.1 - 5.5) 
for i in range(4):
    print("Cluster",i)
    randx = np.random.randint(clusterLower, clusterHigher)
    randy = np.random.randint(clusterLower, clusterHigher)
    randRange = int(np.random.uniform(0.2 * num + 0.5, 0.3 * num + 0.5))
    cluster[i] = Coordinates(randx, randy)
    if len(phoneSet) < 0.70 * num:
        for j in range(randRange):
            posX = cluster[i].xpos + np.random.randint(rangeLower,rangeHigher)
            posY = cluster[i].ypos + np.random.randint(rangeLower,rangeHigher)
            randCost = round(np.random.uniform(0.1 + i + i * 0.5, 1 + i * 1.5), 2)
            newPhone = Phone(posX, posY, randCost)
            phoneSet.add(newPhone)
            for k in range(len(phoneSet)):            
                #print("newPhone",len(phoneSet)-1,"Pinging:",k)
                distance = math.sqrt(math.pow(newPhone.xpos - list(phoneSet)[k].xpos, 2) + math.pow(newPhone.ypos - list(phoneSet)[k].ypos, 2))
                if distance <= newPhone.range:
                    newPhone.addPhone(list(phoneSet)[k])
                    list(phoneSet)[k].addPhone(newPhone)
            print("Generated Phone:", len(phoneSet) -1, "xpos:", newPhone.xpos, "ypos:", newPhone.ypos, "cost:", newPhone.cost)
    else:
        randx = np.random.randint(clusterLower,clusterHigher)
        randy = np.random.randint(clusterLower,clusterHigher)
        cluster[i] = Coordinates(randx, randy)
        for j in range(num - len(phoneSet)):
            posX = cluster[i].xpos + np.random.randint(rangeLower,rangeHigher)
            posY = cluster[i].ypos + np.random.randint(rangeLower,rangeHigher)
            randCost = round(np.random.uniform(0.1 + i + i * 0.5, 1 + i * 1.5),2)
            newPhone = Phone(posX, posY, randCost)  
            phoneSet.add(newPhone)          
            for k in range(len(phoneSet)):
                #print("newPhone",len(phoneSet)-1,"Pinging:",k)
                distance = math.sqrt(math.pow(newPhone.xpos - list(phoneSet)[k].xpos, 2) + math.pow(newPhone.ypos - list(phoneSet)[k].ypos, 2))
                if distance <= newPhone.range:
                    newPhone.addPhone(list(phoneSet)[k])
                    list(phoneSet)[k].addPhone(newPhone)
            print("Generated Phone:", len(phoneSet) -1, "xpos:", newPhone.xpos, "ypos:", newPhone.ypos, "cost:", newPhone.cost)

for i in range(len(phoneSet)):
    print("Phone:", i, "numInRange:", list(phoneSet)[i].numInRange, "cost:", list(phoneSet)[i].cost, "costPerPhone:", list(phoneSet)[i].costPerPhone)


tempSet = phoneSet.copy()
purchaseSet = set()
match algorithmType:
    

    case 0:
        #greedy area algorithm
        #makes a copy of phoneSet called tempSet
        #while the budget is greater than 0,
        #it first checks if tempSet is empty, if not then continue
        #skims through tempSet for phone with the lowest cost per phone 
        #checks if the cost of the phone will break the budget, if not then continue
        #subtract cost from budget and add phone to purchasedSet
        #discards any phones within range of the purchased phone form the tempSet
        #repeat until out of phones
        while budget > 0:
            print("Budget:", round(budget, 2),"tempSet len:", len(tempSet))
            if len(tempSet) == 0:
                print("length break")
                break
            cheapest = list(tempSet)[0]
            for i in range(len(tempSet)):
                if list(tempSet)[i].costPerPhone < cheapest.costPerPhone:
                    cheapest = list(tempSet)[i]
            if budget - cheapest.cost < 0:
                print("Attempt Purchase:", cheapest,"numInRange:", cheapest.numInRange, "cost:", cheapest.cost, "costPerPhone:", cheapest.costPerPhone)
                tempSet.remove(cheapest)
            else:
                budget -= cheapest.cost
                purchaseSet.add(cheapest)
                print("Purchased Phone:", cheapest,"numInRange:", cheapest.numInRange, "cost:", cheapest.cost, "costPerPhone:", cheapest.costPerPhone)
                tempSet = tempSet.difference(cheapest.inRangeSet)
            print("Purchased Set:", purchaseSet)      
    case 1:
        #slopy greedy algorithm Ethan
        while budget > 0:
            cheapest = list(tempSet)[0]
            for i in range(len(tempSet)):
                if list(tempSet)[i].cost < cheapest.cost:
                    cheapest = list(tempSet)[i]
            if budget > cheapest.cost: 
                budget -= cheapest.cost
                purchaseSet.add(cheapest)
                tempSet.discard(cheapest)
                print("Purchased phone: ", cheapest, "cost: ", cheapest.cost)
                print("Budget: ",budget)
            elif budget < cheapest.cost:
                break

    case 2:
        #pure random algorithm Gabriel

        for i in range(len(tempSet)):
            rn = random.randint(0,len(tempSet))
            randPhone = list(tempSet)[rn-1]

            if budget > randPhone.cost: 
                budget -= randPhone.cost
                purchaseSet.add(randPhone)
                tempSet.discard(randPhone)
                print(randPhone, randPhone.cost)
            elif budget < randPhone.cost:
                continue
        
        #print out the nodes to graph 

        print("test")
    case _:
        print("Invalid")

#Graph========================================================
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