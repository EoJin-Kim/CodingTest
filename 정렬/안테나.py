n=int(input())
data=list(map(int,input().split()))
data.sort()
# 인덱스는 시작은 0 부터 이므로
print(data[(n-1)//2])