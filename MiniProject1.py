class Phone:
    radius = 5
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos

phoneArr = [Phone] * 100



arr = [ [0]*1000 for i in range(1000)] 

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = Phone()

        


        
