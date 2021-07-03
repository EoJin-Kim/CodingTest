


def solution(n, results):
    answer = 0
    INF = int(1e9)
    # 노드 개수

    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0

    for a,b in results:

        graph[a][b] = 1
        graph[b][a]=-1

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if graph[a][k]==1 and graph[k][b]==1:
                    graph[a][b]=1
                    graph[b][a]=-1
                elif graph[a][k]==-1 and graph[k][b]==-1:
                    graph[a][b]=-1
                    graph[b][a]=1

    for i in graph:
        if i.count(INF)==1:
            answer+=1

    return answer
print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))