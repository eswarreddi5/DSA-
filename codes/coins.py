def coinschange(totalnumber,coins):
    n = totalnumber
    coins.sort()
    index = len(coins)-1
    while True:
        coinvalue  = coins[index]
        if n>=coinvalue:
            print(coinvalue)
            n = n-coinvalue
        if n<coinvalue:
            index-=1
        if n==0:
            break
coins = [1,2,5,10,20,50,100]
#coinschange(201,coins)

def coindp(n,denoms):
    num_coins = [float("inf")]*(n+1)
    num_coins[0] = 0
    for coin in denoms:
        for current_amount in range(coin,n+1):
            num_coins[current_amount] = min(num_coins[current_amount],num_coins[current_amount-coin]+1)
    return num_coins[n] if num_coins[n]!=float("inf") else -1
print(coindp(6,[1,5]))


def numofways(n,denoms):
    num_coins = [0]*(n+1)
    num_coins[0] = 1
    for coin in denoms:
        for amount in range(coin,n+1):
            num_coins[amount] += num_coins[amount-coin]
    return num_coins[n]
print(numofways(6,[1,5]))


def mincosttickets(days,cost):
    dp = [0]*(days[-1]+1)
    travel_days = set(days)
    for i in range(1,days[-1]+1):
        if i not in travel_days:
            dp[i] = dp[i-1]
        else:
            dp[i] = min(dp[i-1]+cost[0]
                        ,dp[max(0,i-7)]+cost[1],
                        dp[max(0,i-30)]+cost[2])
    return dp[days[-1]]



days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
print(mincosttickets(days,costs))