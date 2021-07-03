# 간선으로 계산하면 다익스트라
# 그래프로 계산하면 플로이드 워셜

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선의 개수
n,m=map(int,input().split())

start=int(input())
graph=[[] for _ in range(n+1)]
distance = [INF]*(n+1)
for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))


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

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])