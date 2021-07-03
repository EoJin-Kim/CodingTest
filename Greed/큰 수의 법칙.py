n,m,k= map(int,input().split())

data=list(map(int,input().split()))

data.sort(reverse=True)
first=data[0]
second=data[1]

result=0

# 큰수가 더해지는 횟수
count = int(m/(k+1))*k
count+=m%(k+1)


result+=(count)*first
result+=(m-count)*second
print(result)
