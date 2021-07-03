import heapq
n=int(input())
heap=[]

for i in range(n):
    heapq.heappush(heap,int(input()))

result=0


while len(heap)!=1:
    one=heapq.heappop(heap)
    two= heapq.heappop(heap)
    sum = one+two
    result+=sum
    heapq.heappush(heap,sum)

print(result)
#30 + 70 + 120