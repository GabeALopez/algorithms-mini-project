import random
class Node:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.range = 50
        self.price = 0 

phoneArr = [Node] * 100

for i in range(100):
    randx = random.randint(0, 1000)
    randy = random.randint(0, 1000)
    phoneArr[i] = Node(randx, randy)
    print("Node", i, "x:", phoneArr[i].xpos, "y:", phoneArr[i].ypos)



print("Node 1", "x:", phoneArr[1].xpos, "y:", phoneArr[1].ypos)

# arr = [ [0]*1000 for i in range(1000)] 

# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         arr[i][j] = Phone()

        


        
