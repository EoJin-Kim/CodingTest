INF=int(1e9)
# 노드, 간선
n,m=map(int,input().split())


graph=[[INF] *(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
print(graph)


for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])


result =0
print(graph)
for i in range(1,n+1):
    count=0
    for j in range(1,n+1):
        if graph[i][j]!=INF or graph[j][i] !=INF:
            count+=1
    if count==n:
        result+=1


print (result)