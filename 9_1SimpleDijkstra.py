import sys
#input = sys.stdin.readline().rstrip()
INF = int(1e9)
# n 노드 개수
# m 간선 개수

n,m = map(int,input().split())
start = int(input())

graph = [[]for i in range(n+1)]
#print(graph)
visited = [False] *(n+1)
distance = [INF]*(n+1)
for _ in range(m):
    # a 노드에서 b 노드로 가는 비용이 c 라는 의미
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value=INF
    index=0
    for i in range(1,n+1):
        if distance[i]<min_value and not visited[i]:
            min_value = distance[i]
            index=i
    return index

def dijkstra(start):
    distance[start]=0
    visited[start] = True

    # 초기 시작점에서 접근 가능한 노드 거리
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 제외해서 n-1개 for문
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True

        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])







