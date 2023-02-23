import random
import math 
        
class Coordinates:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
class Phone(Coordinates):
    def __init__(self,num, xpos, ypos, cost):
        Coordinates.__init__(self, xpos, ypos)
        self.cost = cost
        self.costPerPhone = 0
        self.range = 50
        self.visited = bool(0)
        self.inRangeSet = set()
        self.numInRange = 0       
    def findCPF(self):
        self.costPerPhone = round(self.cost/(self.numInRange + 1), 2)
        
num = 100

phoneArr = [Phone] * num
neighborhood = [Coordinates] * 4

#makes cluster of Phones in Neighborhoods with different costs
k = 0
for i in range(4):
    print("Neighborhood",i)
    randx = random.randint(200, 800)
    randy = random.randint(200, 800)
    neighborhood[i] = Coordinates(randx, randy)
    if k < 0.70 * num:
        for j in range(int(random.uniform(0.2 * num + 0.5, 0.3 * num + 0.5))):
            posX = neighborhood[i].xpos + random.randint(-100,100)
            posY = neighborhood[i].ypos + random.randint(-100,100)
            randCost = round(random.uniform(0.1 + i + i * 0.5, 1 + i * 1.5), 2)
            phoneArr[k] = Phone(num, posX, posY, randCost)
            print("Phone:", k, "cost:",phoneArr[k].cost)
            k += 1
    else:
        randx = random.randint(200, 800)
        randy = random.randint(200, 800)
        neighborhood[i] = Coordinates(randx, randy)
        for j in range(num - k):
            posX = neighborhood[i].xpos + random.randint(-100,100)
            posY = neighborhood[i].ypos + random.randint(-100,100)
            randCost = round(random.uniform(0.1 + i + i * 0.5, 1 + i * 1.5),2)
            phoneArr[k] = Phone(num, posX, posY, randCost)
            print("Phone:", k, "cost:",phoneArr[k].cost)
            k += 1

#makes set for each Phone of Phones that are within range
for i in range(num):
    for j in range(num):
        if (i != j):
            distance = math.sqrt(math.pow(phoneArr[i].xpos - phoneArr[j].xpos, 2) + math.pow(phoneArr[i].ypos - phoneArr[j].ypos, 2))
            if (distance <= phoneArr[i].range):
<<<<<<< Updated upstream
                phoneArr[i].inRangeArr[j] = bool(1)
                phoneArr[i].numInRange = phoneArr[i].numInRange + 1
            if phoneArr[i].numInRange > 0:
                phoneArr[i].costPerNode = round(phoneArr[i].cost / phoneArr[i].numInRange, 2)
            else:
                phoneArr[i].costPerNode = phoneArr[i].cost
            
=======
                phoneArr[i].inRangeSet.add(phoneArr[j])
                phoneArr[i].numInRange = len(phoneArr[i].inRangeSet)
                
>>>>>>> Stashed changes
for i in range(num):
    phoneArr[i].findCPF()

for i in range(num):
    print("Phone:", i, "numInRAnge:", phoneArr[i].numInRange, "cost:", phoneArr[i].cost, "costPerPhone:", phoneArr[i].costPerPhone)

purchaseSet = set()
budget = 10
tempSet = set()
for i in range(num):
    tempSet.add(phoneArr[i])

cheapest = list(tempSet)[i]
#while len(tempSet) > 0:
#    cheapest = list(tempSet)[0]
for i in range(len(tempSet)):
    if list(tempSet)[i].costPerPhone < cheapest.costPerPhone:
        cheapest = list(tempSet)[i]
    
        
print(cheapest.costPerPhone)


#test print
#print("Phone",num - 1,  "x:", phoneArr[num - 1].xpos, "y:", phoneArr[num - 1].ypos, "numInRange:", phoneArr[num - 1].numInRange, "cost:", phoneArr[num - 1].cost, "costperPhone:", phoneArr[num - 1].costPerPhone)


        
