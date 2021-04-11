import sys
input = sys.stdin.readline

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


v,e = map(int,input().split())
parent = [0]*(v+1)

#부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i

# 사이클 발생 여부
cycle = False

for i in range(e):
    a,b = map(int,input().split())

    if find_parent(parent,a) ==find_parent(parent,b):
        cycle = True

    else:
        union_parent(parent,a,b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 발생 x")