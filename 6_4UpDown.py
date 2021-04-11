n=int(input())
result=[]
for i in range(n):
    result.append(int(input()))

result.sort(reverse=True)
for i in result:
    print(i,end=' ')
