def FindParent(parent,x):
    if parent[x]!=x:
        FindParent(parent,parent[x])
    return parent[x]


def UnionParent(parent,a,b):
    a = FindParent(parent,a)
    b=FindParent(parent,b)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a


n,m = map(int,input().split())
parent = [0]*(n+1)
for i in range(1,n+1):
    parent[i] = i

for _ in range(m):
    oper,a,b = map(int,input().split())
    if oper==0:
        UnionParent(parent,a,b)

    elif oper ==1:
        if FindParent(parent,a) ==FindParent(parent,b):
            print("YES")

        else:
            print("NO")