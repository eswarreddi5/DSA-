def recursive(n):
    if n<1:
        print("n is lessthan one.")
    else:
        recursive(n-1)
        print(n)
#recursive(4)


def decimaltobinary(n):
    assert int(n)==n,"number should be positive integer."
    if n==0:
        return 0
    else:
        return n%2 +10*decimaltobinary(int(n/2))
print(decimaltobinary(45))