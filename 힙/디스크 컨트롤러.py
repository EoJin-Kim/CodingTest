import heapq
#1. 대기 시간이 없는 시간이 적은 순서대로 실행



def solution(jobs):
    answer = 0
    length=len(jobs)
    check = [False] * length
    for i in range(len(jobs)):
        jobs[i]=jobs[i][::-1]
        jobs[i].append(i)
    hq=[]
    time=0
    count=0
    result=0

    while count < len(jobs):
        for i in range(length):
            if  time>=jobs[i][1] and check[i]==False :
                heapq.heappush(hq,jobs[i])
                #check[i]=True

        if hq:
            work,wait,idx = heapq.heappop(hq)
            result+= work+ time-wait
            time += work
            count+=1
            check[idx] = True
            hq=[]
        else:
            time+=1

    return result//length


print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[0, 10], [4, 10], [15, 2], [5, 11]]))
#print(solution([[0, 3], [3, 3], [6, 6], [15,6]]))