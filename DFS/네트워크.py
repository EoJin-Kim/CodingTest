
def dfs(node,array,visited):
    for x in node:
        if visited[x]:
            continue
        visited[x]=True
        dfs(array[x],array,visited)
def solution(n, computers):
    answer = 0
    array=[[] for _ in range(n)]
    visited=[False]*n
    row=len(computers)
    col=len(computers[0])
    for i in range(row):
        for j in range(col):
            if i==j:
                continue
            if computers[i][j]!=0:
                array[i].append(j)
    idx=0
    for i in range(n):
        if visited[i]:
            continue
        idx+=1
        visited[i]=True
        dfs(array[i],array,visited)
    return idx
print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))