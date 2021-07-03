import math
n=1000 #2부터 n 까지의 모든 소수를 판별
array=[True for _ in range(n+1)] #처음은 모든 소수를 True로 초기화 0,1 은 제외

for i in range(2,int(math.sqrt(n))+1):
    j=2
    while i*j <=n:
        array[i*j]=False
        j+=1

for i in range(2,n+1):
    if array[i]:
        print(i,end=" ")