# 간선으로 계산하면 다익스트라 # 한 노드에서 모든노드 최단경로
# 그래프로 계산하면 플로이드 워셜 # 모든노드에서 모든노드 최단경로

INF=int(1e9)
# 노드 개수
n=int(input())
# 간선 개수
m=int(input())

graph=[[INF] *(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

for _ in range(m):
    a,b,c=map(int,input().split())
    if graph[a][b]>c:
        graph[a][b]=c

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])


for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] ==INF:
            print(0,end=" ")
        else:
            print(graph[i][j],end=" ")
    print()