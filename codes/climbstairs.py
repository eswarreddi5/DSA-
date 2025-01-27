def climbstairs(n):
    if n==1:
        return 1
    arr = [0]*n
    arr[0] = 1
    arr[1]  = 2
    for i in range(2,n):
        arr[i]  = arr[i-1]+arr[i-2]
    return arr[n-1]
print(climbstairs(4))


def climb(n,dict1):
    if n in dict1:
        return dict1[n]
    if n==1:
        return 1
    if n==2:
        return 2
    dict1[n] = climb(n-1,dict1)+climb(n-2,dict1)
    return dict1[n]
print(climb(4,{}))