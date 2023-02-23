import random
import math
class Node:
    def __init__(self,num, xpos, ypos, cost):
        self.xpos = xpos
        self.ypos = ypos
        self.cost = cost
        self.costPerNode = 0
        self.range = 50
        self.visited = bool(0)
        self.inRangeArr = [bool] * num
        for i in range(num):
            self.inRangeArr[i] = bool(0)
        self.numInRange = 0
        
class Neighborhood:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        
num = 100

phoneArr = [Node] * num
neighborhood = [Neighborhood] * 4

#makes array of Nodes with random positions
k = 0
for i in range(4):
    print("Neighborhood",i)
    randx = random.randint(200, 800)
    randy = random.randint(200, 800)
    neighborhood[i] = Neighborhood(randx, randy)
    if k < 0.70 * num:
        for j in range(int(random.uniform(0.2 * num + 0.5, 0.3 * num + 0.5))):
            posX = neighborhood[i].xpos + random.randint(-100,100)
            posY = neighborhood[i].ypos + random.randint(-100,100)
            randCost = round(random.uniform(0.1 + i + i * 0.5, 1 + i * 1.5), 2)
            phoneArr[k] = Node(num, posX, posY, randCost)
            print("Phone:", k, "cost:",phoneArr[k].cost)
            k = k + 1
    else:
        randx = random.randint(200, 800)
        randy = random.randint(200, 800)
        neighborhood[i] = Neighborhood(randx, randy)
        for j in range(num - k):
            posX = neighborhood[i].xpos + random.randint(-100,100)
            posY = neighborhood[i].ypos + random.randint(-100,100)
            randCost = round(random.uniform(0.1 + i + i * 0.5, 1 + i * 1.5),2)
            phoneArr[k] = Node(num, posX, posY, randCost)
            print("Phone:", k, "cost:",phoneArr[k].cost)
            k = k + 1
        
for i in range(num):
    for j in range(num):
        if (i != j):
            distance = math.sqrt(math.pow(phoneArr[i].xpos - phoneArr[j].xpos, 2) + math.pow(phoneArr[i].ypos - phoneArr[j].ypos, 2))
            if (distance <= phoneArr[i].range):
                phoneArr[i].inRangeArr[j] = bool(1)
                phoneArr[i].numInRange = phoneArr[i].numInRange + 1
            if phoneArr[i].numInRange > 0:
                phoneArr[i].costPerNode = round(phoneArr[i].cost / phoneArr[i].numInRange, 2)
            else:
                phoneArr[i].costPerNode = phoneArr[i].cost
            
for i in range(num):
    print("Node ", i, ":", end=" ")
    for j in range(num):
        print(int(phoneArr[i].inRangeArr[j]), end="")
    print("\n")

#test print
print("Node",num - 1,  "x:", phoneArr[num - 1].xpos, "y:", phoneArr[num - 1].ypos, "numInRange:", phoneArr[num - 1].numInRange, "cost:", phoneArr[num - 1].cost, "costpernode:", phoneArr[num - 1].costPerNode)

# arr = [ [0]*1000 for i in range(1000)] 

# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         arr[i][j] = Phone()

        


        
