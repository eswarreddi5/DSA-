def knapscak(values,weights,capacity):
    num_items = len(values)
    dp = [[0 for i in range(capacity+1)] for i in range(num_items+1)]
    for i in range(1,num_items+1):
        for j in range(1,capacity+1):
            if weights[i-1]<=j:
                dp[i][j] = max(values[i-1]+dp[i-1][j-weights[i-1]],dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[num_items][capacity]
values = [60,100,120]
weights = [10,20,30]
capacity = 50
max_value  = knapscak(values,weights,capacity)
print(f"Maximum value:{max_value}")   


def fractionalkanpsack(capacity,items):
    items.sort(key=lambda item:item[0]/item[1],reverse=True)
    total_value = 0.0
    remaining_capacity = capacity
    for value,weight in items:
        if remaining_capacity==0:
            break
        if weight<=remaining_capacity:
            total_value+=value
            remaining_capacity-=weight
        else:
            fraction = remaining_capacity/weight
            total_value+=value*fraction
            remaining_capacity = 0
    return total_value
items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
capacity = 50
max_value = fractionalkanpsack(capacity, items)
print(f"Maximum value: {max_value}")


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