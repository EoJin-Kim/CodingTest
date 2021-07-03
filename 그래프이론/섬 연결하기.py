
def find_parent(x,parent):
    if parent[x]!=x:
        parent[x]=find_parent(parent[x],parent)
    return parent[x]


def union_parent(a,b,parent):
    a=find_parent(a,parent)
    b=find_parent(b,parent)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a

def solution(n, costs):
    answer = 0
    parent=[ i for i in range(n+1)]

    costs.sort(key=lambda x : x[2])
    for cost in costs:
        if find_parent(cost[0],parent)!=find_parent(cost[1],parent):
            union_parent(cost[0],cost[1],parent)
            answer+=cost[2]

    return answer

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
