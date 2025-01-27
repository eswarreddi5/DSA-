def numberfactor(n,dp):
    if n in (0,1,2):
        return 1
    elif n==3:
        return 2
    elif n not in dp:
        subp1 = numberfactor(n-1,dp)
        subp2 = numberfactor(n-3,dp)
        subp3 = numberfactor(n-4,dp)
        dp[n] = subp1+subp2+subp3
    return dp[n]
dp = {}
print(numberfactor(4,dp))

def numberfctor(n):
    tb = [1,1,1,2]
    for i in range(4,n+1):
        tb.append(tb[i-1]+tb[i-3]+tb[i-4])
    return tb[n]
print(numberfctor(7))

##################################
def fibmemo(n,memo):
    if n==1:
        return 0
    elif n==2:
        return 1
    if n not in memo:
        memo[n] = fibmemo(n-1,memo)+fibmemo(n-2,memo)
    return memo[n]
memo = {}
print(fibmemo(6,memo))


def fibtab(n):
    tb = [0,1]
    for i in range(2,n+1):
        tb.append(tb[i-1]+tb[i-2])
    return tb[n-1]
print(fibtab(6))
