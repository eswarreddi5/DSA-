def bubblesort(custlist):
    for i in range(len(custlist)-1):
        for j in range(len(custlist)-i-1):
            if custlist[j]>custlist[j+1]:
                custlist[j],custlist[j+1] = custlist[j+1],custlist[j]
    print(custlist)
custlist = [4,8,5,9,7,10]
bubblesort(custlist)    

def selectionsort(custlist):
    for i in range(len(custlist)):
        min_index = i
        for j in range(i+1,len(custlist)):
            if custlist[min_index]>custlist[j]:
                min_index = j
        custlist[i],custlist[min_index] = custlist[min_index],custlist[i]
    print(custlist)
custlist = [4,8,5,9,7,10]
selectionsort(custlist)    
            