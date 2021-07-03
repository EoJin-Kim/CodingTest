INF=10001
n,m = map(int,input().split())
dp=[INF]*(m+1)
data=[]
for i in range(n):
    data.append(int(input()))

dp[0]=0

for i in range(n):
    for j in range(data[i],m+1):
        if dp[j-data[i]]!=INF:
            dp[j] = min(dp[j-data[i]]+1,dp[j])

if dp[m]==INF:
    print(-1)

else:
    print(dp[m])

