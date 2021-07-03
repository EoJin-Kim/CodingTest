def find_parent(parent,x):
    if parent[x] !=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a= find_parent(parent,a)
    b= find_parent(parent,b)

    if a<b:
        parent[b]=a

    else:
        parent[a]=b

n,e = map(int,input().split())

# parent 테이블 초기화 및 생성
parent=[0] * (n+1)
for i in range(1,n+1):
    parent[i]=i


for i in range(e):

    a,b = map(int,input().split())
    if find_parent(parent,a)==find_parent(parent,b):
        print("Cycle")
    else:
        union_parent(parent,a,b)



