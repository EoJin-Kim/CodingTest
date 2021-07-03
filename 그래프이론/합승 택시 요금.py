def solution(n, s, a, b, fares):

    INF=int(1e9)
    graph=[[INF]*(n+1) for i in range(n+1)]
    for q,w,c in fares:
        graph[q][w]=c
        graph[w][q] = c

    for i in range(1,n+1):
        graph[i][i]=0
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
    answer=INF
    for i in range(1,n+1):
        answer=min(answer,graph[s][i]+graph[i][a]+graph[i][b])
    return answer

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))