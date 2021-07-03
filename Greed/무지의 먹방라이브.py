import heapq

def solution(food_times, k):
    if sum(food_times)<=k:
        return -1

    sumValue=0
    beforeValue=0
    length=len(food_times)
    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))

    # 나머지가 food를 못뺼 때 까지 while
    while sumValue + (q[0][0]-beforeValue)*length<= k:
        now=heapq.heappop(q)[0]
        sumValue+=now*length
        length-=1
        beforeValue=now

    q.sort(key=lambda x : x[1])
    return q[(k-sumValue)%length][1]


print(solution([3,1,2],5))
print(solution([8,6,4],15))