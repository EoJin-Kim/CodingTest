import heapq
import sys
input = sys.stdin.readline
# 노드 개수, 간선의 개수, 거리 정보, 출발 도시
n,m,k,start = map(int,input().split())

INF = int(1e9)


graph=[[] for _ in range(n+1)]
distance = [INF]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))


def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
check=False
for i in range(1,len(distance)):
    if distance[i]==k:
        print(i)
        check=True
if check==False:
    print(-1)