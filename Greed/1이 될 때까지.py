n,k = map(int,input().split())
result = 0


while n>=k:

    while n%k!=0:
        result+=n%k
        n-=n%k

    result+=1
    n=n//k

result+=(n-1)
print(result)

