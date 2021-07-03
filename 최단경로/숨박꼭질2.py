import heapq

n,m=map(int,input().split())

INF=int(1e9)
graph=[[] for i in range(n+1)]
distance=[INF] * (n+1)

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))



def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start]=0
    while q:
        dist,now = heapq.heappop(q)
        if dist>distance[now]:
            continue

        for i in graph[now]:
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))




maxIndex=-1
maxValue=-1
dijkstra(1)
for i in range(1,n+1):
    if maxValue==distance[i]:
        count+=1
    if distance[i]>maxValue:
        maxIndex=i
        count=1
        maxValue=distance[i]


print(maxIndex,maxValue,count)


'''
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''