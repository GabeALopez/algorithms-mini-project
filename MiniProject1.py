import random
import math
class Node:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.cost = 0
        self.range = 50
    def __init__(self, xpos, ypos, cost):
        self.xpos = xpos
        self.ypos = ypos
        self.cost = cost
        self.range = 50


phoneArr = [Node] * 100

#makes array of Nodes with random positions
k = 0
for i in range(0,4):
    print("Neighborhood",i)
    randx = random.randint(200, 800)
    randy = random.randint(200, 800)
    randCost = 0
    neighborhood = Node(randx, randy, randCost)
    if (k < 100 - 30):
        for j in range(0, random.randint(25,30)):
            posX = neighborhood.xpos + random.randint(-100,100)
            posY = neighborhood.ypos + random.randint(-100,100)
            randCost = round(random.uniform(i + i * 0.5, 1 + i * 1.5),1)
            phoneArr[k] = Node(posX, posY, randCost)
            print("Phpne:", k, "cost:",phoneArr[k].cost)
            k = k + 1
    else:
        for j in range(0, 100 - k):
            posX = neighborhood.xpos + random.randint(-100,100)
            posY = neighborhood.ypos + random.randint(-100,100)
            randCost = round(random.uniform(i + i * 0.5, 1 + i * 1.5),1)
            phoneArr[k] = Node(posX, posY, randCost)
            print("Phpne:", k, "cost:",phoneArr[k].cost)
            k = k + 1
        



#test print
print("Node 1", "x:", phoneArr[1].xpos, "y:", phoneArr[1].ypos)

# arr = [ [0]*1000 for i in range(1000)] 

# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         arr[i][j] = Phone()

        


        
