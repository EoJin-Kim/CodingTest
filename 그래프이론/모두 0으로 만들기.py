import sys
sys.setrecursionlimit(300000)
from collections import defaultdict

answer = 0


def dfs(x, a, tree, visited):
    global answer
    visited[x]=1
    for i in tree[x]:
        if not visited[i]:
            a[x]+=dfs(i,a,tree,visited)
    answer += abs(a[x])
    return abs(a[x])

def solution(a, edges):
    global answer

    if sum(a) != 0:
        return -1

    tree = defaultdict(list)

    for i, j in edges:
        tree[i].append(j)
        tree[j].append(i)

    visited = [0] * len(a)

    dfs(0, a, tree, visited)
    return answer

print(solution([-5,0,2,1,2],[[0,1],[3,4],[2,3],[0,3]]))