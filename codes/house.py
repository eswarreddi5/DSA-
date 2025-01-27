def houserobber(houses,curretindex,mydict):
    if curretindex>=len(houses):
        return 0
    else:
        if curretindex not in mydict:   
            stealfirsthouse = houses[curretindex]+houserobber(houses,curretindex+2,mydict)
            skipfirst = houserobber(houses,curretindex+1,mydict)
            mydict[curretindex] = max(stealfirsthouse,skipfirst)
        return mydict[curretindex]
houses = [6,7,1,30,8,2,4]
print(houserobber(houses,0,{}))

def houserob(hou):
    tb = [0]*(len(hou)+2)
    for i in range(len(hou)-1,-1,-1):
        tb[i] = max(hou[i]+tb[i+2],tb[i+1])
    print(tb)
    return tb[0]
houserob([6,1,7,30,8])


def rob(hous):
    rob1,rob2 = 0,0
    for n in hous:
        temp = max(n+rob1,rob2)
        rob1 = rob2
        rob2 = temp
    return rob2
hous = [6,7,1,30,8]
print(rob(hous))