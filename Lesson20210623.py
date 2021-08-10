

pathA1 = ["sa1", "ad1"]
pathA2 = ["sa2", "ad2"]
pathA3 = ["sa3", "ad3"]

allPath = [pathA1, pathA2, pathA3]

cost = { "sa1" : 2, "sa2" : 3, "sa3" : 4, "ad1" : 3, "ad2" : 3, "ad3" : 3 }

#costpath1 = cost["sa1"] +cost["ad1"]
#costpath2 = cost["sa2"] +cost["ad2"]
#costpath3 = cost["sa3"] +cost["ad3"]


for i in range(0, len(allPath)): #allPath -> pathA , B , C
    path = allPath[i] # 
    #print(path)
    sum = 0
    
    # find every item in pathA1 = path
    for j in range(0, len(path)):
        sum=sum+ cost[path[j]]
    if i==0:
        minpath=allPath[i]
        mincost=sum
    else:
        if sum<mincost:
            minpath=allPath[i]
            mincost=sum
print(minpath)
print(mincost)            