import math
def binarysearch(arr,value):
    start = 0
    end = len(arr)-1
    mid = math.floor((start+end)/2)
    while not(arr[mid]==value) and start<=end:
        if value<arr[mid]:
            end = mid-1
        else:
            start = mid+1
        mid = math.floor((start+end)/2)
    if arr[mid]==value:
        return mid
    else:
        return -1
arr = [2,3,1,8,7]
print(binarysearch(arr,8))


def linersearch(arr,value):
    for i in range(len(arr)):
        if arr[i]==value:
            return i
    return -1
arr = [2,3,1,8,7]
print(linersearch(arr,3))
