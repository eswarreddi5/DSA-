def arra(arr):
    subarray = [[]]
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            subarray.append(arr[i:j+1])
    subarray.sort()
    return subarray
arr = []
all_subarrays = arra(arr)
print(f"All possible subarrays of {arr}: {all_subarrays}")

def array(arr):
    subarray = [[]]
    n = len(arr)-1
    for i in range(len(arr)):
        j = i+1
        subarray.append([arr[i]])
        while j<=n:
            subarray.append(arr[i:j+1])
            j+=1
        
    return subarray
arr = [1,2,3,4]
print(array(arr))

def ar(arr):
    return[arr[i:j+1] for i in range(len(arr)) for j in range(i,len(arr))]
print(ar([1,2,3,4]))
