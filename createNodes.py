import random
import math 
        
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
        self.findCPF()
    def removePhone(self, phone):
        self.inRangeSet.discard(phone)
        self.numInRange = len(self.inRangeSet)
        self.findCPF()
    def findCPF(self):
        self.costPerPhone = round(self.cost/(self.numInRange), 2)
        
num = 100
budget = 5

phoneSet = set()
neighborhood = [Coordinates] * 4

#makes cluster of Phones in Neighborhoods with different costs
k = 0
for i in range(4):
    print("Neighborhood",i)
    randx = random.randint(200, 800)
    randy = random.randint(200, 800)
    randRange = int(random.uniform(0.2 * num + 0.5, 0.3 * num + 0.5))
    neighborhood[i] = Coordinates(randx, randy)
    if k + randRange < 0.70 * num:
        for j in range(randRange):
            posX = neighborhood[i].xpos + random.randint(-100,100)
            posY = neighborhood[i].ypos + random.randint(-100,100)
            randCost = round(random.uniform(0.1 + i + i * 0.5, 1 + i * 1.5), 2)
            phoneSet.add(Phone(posX, posY, randCost))
            print("Phone:", k, "cost:",list(phoneSet)[k].cost)
            k += 1
    else:
        randx = random.randint(200, 800)
        randy = random.randint(200, 800)
        neighborhood[i] = Coordinates(randx, randy)
        for j in range(num - k):
            posX = neighborhood[i].xpos + random.randint(-100,100)
            posY = neighborhood[i].ypos + random.randint(-100,100)
            randCost = round(random.uniform(0.1 + i + i * 0.5, 1 + i * 1.5),2)
            phoneSet.add(Phone(posX, posY, randCost))
            print("Phone:", k, "cost:",list(phoneSet)[k].cost)
            k += 1

#makes set for each Phone of Phones that are within range
for i in range(len(phoneSet)):
    for j in range(len(phoneSet)):                
        distance = math.sqrt(math.pow(list(phoneSet)[i].xpos - list(phoneSet)[j].xpos, 2) + math.pow(list(phoneSet)[i].ypos - list(phoneSet)[j].ypos, 2))
        if (distance <= list(phoneSet)[i].range):
            list(phoneSet)[i].addPhone(list(phoneSet)[j])
for i in range(num):
    print("Phone:", i, "numInRange:", list(phoneSet)[i].numInRange, "cost:", list(phoneSet)[i].cost, "costPerPhone:", list(phoneSet)[i].costPerPhone)

#algorithm
tempSet = phoneSet.copy()
purchaseSet = set()
cheapest = list(tempSet)[0]
while budget > 0:
    print("Budget:", round(budget, 2))
    cheapest = list(tempSet)[0]
    for i in range(len(tempSet)):
        if list(tempSet)[i].costPerPhone < cheapest.costPerPhone:
            cheapest = list(tempSet)[i]
    if budget - cheapest.cost < 0:
        break
    else:
        budget -= cheapest.cost
        purchaseSet.add(cheapest)
        print("Purchased Phone:", cheapest,"numInRange:", cheapest.numInRange, "cost:", cheapest.cost, "costPerPhone:", cheapest.costPerPhone)
    tempSet = tempSet.difference(cheapest.inRangeSet)
    tempSet.discard(cheapest)

print("Purchased Set:", purchaseSet)


#test print
#print("Phone",num - 1,  "x:", phoneArr[num - 1].xpos, "y:", phoneArr[num - 1].ypos, "numInRange:", phoneArr[num - 1].numInRange, "cost:", phoneArr[num - 1].cost, "costperPhone:", phoneArr[num - 1].costPerPhone)


        
