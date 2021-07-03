import sys
input = sys.stdin.readline
n = int(input())
dp=[1] * (n)
array=list(map(int,input().split()))
array.reverse()



for i in range(1,n):
    for j in range(i):
        if array[i]>array[j]:
            dp[i]=max(dp[i],dp[j]+1)


print(n-max(dp))
'''
7
15 11 4 8 5 2 4
'''