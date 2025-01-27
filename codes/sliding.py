def maxsubarray(array,k):
    if len(array)<k:
        return 0
    total= sum(array[:k])
    maxtotal = total
    for i in range(len(array)-k):
        total-=array[i]
        total+=array[i+k]
        maxtotal = max(maxtotal,total)
    return maxtotal
array = [1,2,3,4,5,6]
k = 3
print(maxsubarray(array,k))