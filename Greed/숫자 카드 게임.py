n,m=map(int,input().split())
array=[]
for _ in range(n):
    temp=min(list(map(int,input().split())))
    array.append(temp)

print(max(array))

