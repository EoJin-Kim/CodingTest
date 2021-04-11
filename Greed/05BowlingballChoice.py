from collections import Counter
#n,m =  map(int,input().split())
#data = list(map(int,input().split()))
#n,m = 5,3
#data=[1,2,3,3,2]
n,m = 8,5
data=[1,5,4,3,2,4,5,2]
#dataSet=set(data)
countInfo = Counter(data)
result=0
print(countInfo)
for i in range(1,m+1):

    n-=countInfo[i]
    result+=countInfo[i]*n

print(result)
