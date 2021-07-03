n=int(input())


data=[]
for i in range(n):
    name,score=input().split()
    data.append((name,score))

def sortfunc(data):
    return data[1]
data.sort(key=sortfunc)

for i in data:
    print(i[0],end=" ")