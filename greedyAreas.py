overallSet = []
setEmpty = []
holdSet = []
cost = 0
cost2 = 0
budget = 50
weight = 0
maximize = 0

while holdSet.count() != 0:
    maximize = weight/cost2
    if (cost + cost2) <= budget:
        setEmpty = setEmpty.union(overallSet)
        cost += cost2
    holdSet /= overallSet

print(setEmpty)
    
