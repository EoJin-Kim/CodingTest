def solution(n, times):
    answer = 0

    maxTime = max(times)
    start=0
    end=maxTime*n
    while start<=end:
        mid=(start+end)//2
        count=0
        for i in times:
            count += mid // i
            if count>n:break

        if count<n:
            start=mid+1

        else:
            answer=mid
            end = mid-1
    return answer




print(solution(6,[7,10]))