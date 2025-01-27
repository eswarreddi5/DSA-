def kanpsack(capacity,profits,weights):
    dp = [[0 for i in range(capacity+1)] for j in range(len(weights)+1)]
    #dp = [[0 for i in range(capacity+1)] for i in range(num_items+1)]
    for i in range(1,len(profits)+1):
        for j in range(1,capacity+1):
            if weights[i-1]>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(profits[i-1]+dp[i-1][j-weights[i-1]],dp[i-1][j])
    return dp[len(profits)][capacity]
values = [60,100,120]
weights = [10,20,30]
capacity = 50
print(kanpsack(capacity,values,weights))



def fractionalkanpsack(capactiy,items):
    items.sort(key=lambda item:item[0]/item[1],reverse=True)
    tottalvalue = 0.0
    remaining_capactiy = capacity
    for profit,weight in items:
        if remaining_capactiy==0:
            break
        if weight<=remaining_capactiy:
            tottalvalue+=profit
            remaining_capactiy-=weight
        else:
            ratio = remaining_capactiy/weight
            tottalvalue += profit*ratio
            remaining_capactiy=0
        return tottalvalue

items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
capacity = 50
max_value = fractionalkanpsack(capacity, items)
print(f"Maximum value: {max_value}")