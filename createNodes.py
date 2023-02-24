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
        
num = 10000
budget = 50

phoneSet = set()
neighborhood = [Coordinates] * 4

#makes cluster of Phones in Neighborhoods with different costs
for i in range(4):
    print("Neighborhood",i)
    randx = random.randint(200, 800)
    randy = random.randint(200, 800)
    randRange = int(random.uniform(0.2 * num + 0.5, 0.3 * num + 0.5))
    neighborhood[i] = Coordinates(randx, randy)
    if len(phoneSet) < 0.70 * num:
        for j in range(randRange):
            posX = neighborhood[i].xpos + random.randint(-100,100)
            posY = neighborhood[i].ypos + random.randint(-100,100)
            randCost = round(random.uniform(0.1 + i + i * 0.5, 1 + i * 1.5), 2)
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
        randx = random.randint(200, 800)
        randy = random.randint(200, 800)
        neighborhood[i] = Coordinates(randx, randy)
        for j in range(num - len(phoneSet)):
            posX = neighborhood[i].xpos + random.randint(-100,100)
            posY = neighborhood[i].ypos + random.randint(-100,100)
            randCost = round(random.uniform(0.1 + i + i * 0.5, 1 + i * 1.5),2)
            newPhone = Phone(posX, posY, randCost)  
            phoneSet.add(newPhone)          
            for k in range(len(phoneSet)):
                #print("newPhone",len(phoneSet)-1,"Pinging:",k)
                distance = math.sqrt(math.pow(newPhone.xpos - list(phoneSet)[k].xpos, 2) + math.pow(newPhone.ypos - list(phoneSet)[k].ypos, 2))
                if distance <= newPhone.range:
                    newPhone.addPhone(list(phoneSet)[k])
                    list(phoneSet)[k].addPhone(newPhone)
            print("Generated Phone:", len(phoneSet) -1, "xpos:", newPhone.xpos, "ypos:", newPhone.ypos, "cost:", newPhone.cost)

#makes set for each Phone of Phones that are within range
# for i in range(len(phoneSet)):
#     for j in range(len(phoneSet)):                
#         #print("Phone:",i,"Pinging",j)
#         distance = math.sqrt(math.pow(list(phoneSet)[i].xpos - list(phoneSet)[j].xpos, 2) + math.pow(list(phoneSet)[i].ypos - list(phoneSet)[j].ypos, 2))
#         if (distance <= list(phoneSet)[i].range):
#             list(phoneSet)[i].addPhone(list(phoneSet)[j])
for i in range(len(phoneSet)):
    print("Phone:", i, "numInRange:", list(phoneSet)[i].numInRange, "cost:", list(phoneSet)[i].cost, "costPerPhone:", list(phoneSet)[i].costPerPhone)

#algorithm
tempSet = phoneSet.copy()
purchaseSet = set()
cheapest = list(tempSet)[0]
while budget > 0:
    print("Budget:", round(budget, 2),"tempSet len:", len(tempSet))
    if len(tempSet) == 0:
        print("len break")
        break
    cheapest = list(tempSet)[0]
    for i in range(len(tempSet)):
        if list(tempSet)[i].costPerPhone < cheapest.costPerPhone:
            cheapest = list(tempSet)[i]
    if budget - cheapest.cost < 0:
        print("attempt purchase:", cheapest.cost)
        print("budget break")
        break
    else:
        budget -= cheapest.cost
        purchaseSet.add(cheapest)
        print("Purchased Phone:", cheapest,"numInRange:", cheapest.numInRange, "cost:", cheapest.cost, "costPerPhone:", cheapest.costPerPhone)
    tempSet = tempSet.difference(cheapest.inRangeSet)
    tempSet = tempSet.difference(purchaseSet)

print("Purchased Set:", purchaseSet)


#test print
#print("Phone",num - 1,  "x:", phoneArr[num - 1].xpos, "y:", phoneArr[num - 1].ypos, "numInRange:", phoneArr[num - 1].numInRange, "cost:", phoneArr[num - 1].cost, "costperPhone:", phoneArr[num - 1].costPerPhone)


        
