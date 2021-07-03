import heapq
from collections import Counter
INF=int(1e9)
def solution(n, edge):
    answer = 0
    distance=[INF for i in range(n+1)]
    graph=[[] for _ in range(n+1)]
    for a,b in edge:
        graph[a].append((b,1))
        graph[b].append((a, 1))
        #graph[b][a]=1

    q=[]
    distance[1] = 0
    heapq.heappush(q,(0,1))
    while q:
        dist,now=heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                heapq.heappush(q,(cost,i[0]))
                distance[i[0]]=cost

    for i in range(len(distance)):
        if distance[i]==INF:
            distance[i]=-1
    maxDistance=max(distance)
    return distance.count(maxDistance)

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))