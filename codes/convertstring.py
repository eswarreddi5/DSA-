def convert(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][m] = n-i
    for j in range(m+1):
        dp[n][j] = m-j
    
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if s1[i]==s2[j]:
                dp[i][j] = dp[i+1][j+1]
            else:
                dp[i][j] = 1+min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])
    return dp[0][0]
s1 = "eswar"
s2 = "chaitu"
print(convert(s1,s2))
