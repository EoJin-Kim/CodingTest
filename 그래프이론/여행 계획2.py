def FindParent(parent,x):

    if parent[x] != x:
        parent[x] =FindParent(parent,parent[x])
    return parent[x]



def UnionParent(parent,a,b):
    a=FindParent(parent,a)
    b=FindParent(parent,b)
    if a<b:
        parent[b]=a

    else:
        parent[a]=b

n,m = map(int,input().split())


graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

plan=list(map(int,input().split()))


parent=[0]*(n+1)

for i in range(1,n+1):
    parent[i]=i

for a in range(n):
    for b in range(n):
        if graph[a][b]!=0:
            UnionParent(parent,a+1,b+1)

result =True
for p in range(len(plan)-1):
    a=FindParent(parent,plan[p+1])
    b=FindParent(parent,plan[p])
    if a!=b:
        result=False
        break

if result:
    print("YES")
else:
    print("NO")
print(parent)
"""
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
"""