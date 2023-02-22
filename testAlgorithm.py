class Node:
  radius = 5;
  def __init__(self,xpos,ypos,price):
    self.xpos = xpos;
    self.ypos = ypos;
    self.price = price;

#temp layout array
#rows, cols = (10, 10)
#arr = [[Node(i,j,0) for i in range(cols)] for j in range(rows)]
    
#array to contain Nodes
nodeArr = [100];

#temp stuff
countX = 0;
countY = 0;
priceCount = 0.1;

#initializing Nodes
for int in range(0,99):
  Node(countX,countY,priceCount)
  countX + countX + 1;
  if(countX > 10):
    countX = 0;
    countY = countY + 1;
  priceCount = priceCount + priceCount;
  nodeArr[int] = Node; #errors
  print(int);

#print nodes
for node in nodeArr:
  print(nodeArr[node].xpos);