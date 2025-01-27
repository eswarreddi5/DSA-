def heapify(custlist,n,i):
    max = i
    left = 2*i+1
    right = 2*i+2
    if left<n and custlist[max]<custlist[left]:
        max = left
    if right<n and custlist[max]<custlist[right]:
        max = right
    if max!=i:
        custlist[max],custlist[i] = custlist[i],custlist[max]
        heapify(custlist,n,max)
def buildmax(custlist):
    n = len(custlist)
    for i in range(n//2-1,-1,-1):
        heapify(custlist,n,i)
def heapsort(custlist):
    n = len(custlist)
    buildmax(custlist)
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(custlist,i,0)
arr = [2,1,3,8,7]
heapsort(arr)
print(arr)
    