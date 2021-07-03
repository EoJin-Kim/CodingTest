
def stone_check(num,stones,k):
    cnt=0
    for i in range(len(stones)):
        if stones[i]<num:
            cnt+=1
        else:
            cnt=0
        if cnt>=k:
            return False
    return True

def solution(stones, k):
    answer = -int(1e9)

    start=1
    end=200000000
    while start<=end:
        mid=(start+end)//2
        if stone_check(mid,stones,k):
            answer=max(mid,answer)
            start = mid + 1
        else:
            end = mid - 1


    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	,3))