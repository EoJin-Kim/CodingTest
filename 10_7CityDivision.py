
def FindParent(parent,x):
    if parent[x]!=x:
        parent[x] =FindParent(parent,parent[x])
    return parent[x]

def UnionParent(parent,a,b):
    a = FindParent(parent,a)
    b= FindParent(parent,b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b
result = 0
edges=[]

n,m = map(int, input().split())

parent = [0] *(n+1)

for i in range(1,n+1):
    parent[i] = i


for _ in range(m):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()
print(edges)

last = 0
for edge in edges:
    cost,a,b = edge
    if FindParent(parent,a) !=FindParent(parent,b):
        UnionParent(parent,a,b)
        result+=cost
        last =cost

print(result-last)



