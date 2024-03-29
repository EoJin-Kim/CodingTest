n=int(input())
INF=int(1e9)
graph=[[INF]*(n+1) for i in range(n+1)]

m=int(input())

for i in range(m):
    a,b,c=map(int,input().split())
    if graph[a][b]>c:
        graph[a][b]=c

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0
print(graph)
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])


for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]>=INF:
            print(-1,end=" ")
        else:
            print(graph[i][j],end=" ")
    print()
