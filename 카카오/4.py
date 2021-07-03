import heapq
from collections import deque
INF = int(1e9)


def solution(n, start, end, roads, traps):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)

    for road in roads:
        a, b, c = road
        graph[a].append((b, c))
    q=deque([])
    q.append((0,start))
    distance[start]=0
    while q:
        trap=False
        dist,now=q.popleft()
        if distance[end]!=INF:
            break
        if now in traps:
            check = []
            for a in range(len(graph[now])):
                temp = graph[i[0]].pop(a)
                graph[temp[0]].append((i[0], temp[1]))
                check.append(temp[0])
            for a in range(len(graph)):
                for b in range(len(graph[a])):

                    if graph[a][b][0] == i[0]:
                        if a in check:
                            continue
                        temp = graph[a].pop(b)
                        graph[temp[0]].append((a, temp[1]))

        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
            q.append((cost,i[0]))
                #heapq.heappush(q,(cost,i[0]))

    return distance[end]

#print(solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2]))
print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2, 3]))