from createNodes import Node
from createNodes import phoneArr
import math
import numpy as np

for i in range(100):
    for j in range(100):
        if (i != j):
            distance = math.sqrt(math.pow(phoneArr[i].xpos - phoneArr[j].xpos, 2) + math.pow(phoneArr[i].ypos - phoneArr[j].ypos, 2))
            if (distance <= phoneArr[i].range/2):
                phoneArr[i].inRangeArr[j] = bool(1)
            
for i in range(100):
    print("Node ", i, ":", end=" ")
    for j in range(100):
        print(int(phoneArr[i].inRangeArr[j]), end="")
    print("\n")
    
        