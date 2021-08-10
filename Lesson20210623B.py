

pathA1B1 = ["sa1", "a1b1", "b1d"] #9
pathA1B2 = ["sa1", "a1b2", "b2d"] #12
pathA1B3 = ["sa1", "a1b3", "b3d"] #7
pathA2B1 = ["sa2", "a2b1", "b1d"] #8
pathA2B2 = ["sa2", "a2b2", "b2d"] #11
pathA2B3 = ["sa2", "a2b3", "b3d"] #9
pathA3B1 = ["sa3", "a3b1", "b1d"] #10
pathA3B2 = ["sa3", "a3b2", "b2d"] #11
pathA3B3 = ["sa3", "a3b3", "b3d"] #15


allPath = [pathA1B1, pathA1B2, pathA1B3, pathA2B1, pathA2B2, pathA2B3, pathA3B1, pathA3B2, pathA3B3]

cost = { "sa1" : 2, "sa2" : 3, "sa3" : 4, "b1d" : 3, "b2d" : 3, "b3d" : 3, 
        "a1b1" : 4, "a1b2" : 7, "a1b3" : 2, "a2b1" : 2, "a2b2" : 5, "a2b3" : 3,
        "a3b1" : 3, "a3b2" : 4, "a3b3" : 8}

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