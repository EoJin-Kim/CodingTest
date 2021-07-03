import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
k=0
data.sort()
result=0
for i in data:
    k+=1
    if k==i:
        result+=1
print(result)