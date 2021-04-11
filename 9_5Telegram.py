import sys
import heapq
INF=int(1e9)
input = sys.stdin.readline
n,m,k = map(int,input().split())

graph = [[] for _ in range(n+1)]
distance =[INF for i in range(n+1)]
for _ in range(m):
    x,y,z, = map(int,input().split())
    graph[x].append((y,z))


def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while(q):
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist +i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(k)
print(distance)
maxDistance=0
count=0
for i in distance:
    if i !=INF:
        count +=1
        maxDistance=max(maxDistance,i)

print(count-1,maxDistance)
