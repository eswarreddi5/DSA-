def lcs(s1,s2,n,m):
    if n<0 or m<0:
        return 0
    if s1[n]==s2[m]:
        return 1+lcs(s1,s2,n-1,m-1)
    return max(lcs(s1,s2,n-1,m),lcs(s1,s2,n,m-1))
s1 = "acd"
s2 = "ced"
print("the longest common subsequence is",lcs(s1,s2,len(s1)-1,len(s2)-1))


def lcsb(s1,s2):
   n,m = len(s1),len(s2)
   dp = [[-1 for i in range(m+1)]for j in range(n+1)]
   for i in range(n+1):
       dp[i][0] = 0
   for j in range(m+1):
       dp[0][j] = 0
   for n in range(1,n+1):
       for m in range(1,m+1):
           if s1[n-1]==s2[m-1]:
               dp[n][m] = 1+dp[n-1][m-1]
           else:
               dp[n][m] = max(dp[n-1][m],dp[n][m-1])
   i,j = n,m
   stri = ""
   while i>0 and j>0:
       if s1[i-1]==s2[j-1]:
           stri = stri+s2[j-1]
           i-=1
           j-=1
       else:
           if dp[i-1][j]>dp[i][j-1]:
               i-=1
           else:
               j-=1
   return stri[::-1]

s1 = "bbabcbcab"
s2 = s1[::-1]
print("the longest common subsequence is",lcsb(s1,s2))




