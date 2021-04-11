INF = int(1e9)


# 노드의 개수 및 간선의 개수
n = int(input())
m = int(input())

graph=[[INF] *(n+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i==j:
            graph[i][j]=0
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b]=c
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])


for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print("INFINITY",end=" ")
        else:
            print(graph[a][b],end=" ")
    print()