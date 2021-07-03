
def solution(nums):
    answer = 0
    length = len(nums)
    q = []
    nums = set(nums)
    if len(nums)>length//2:
        return length//2
    else:
        return len(nums)


    return answer


print(solution([3,3,3,2,2,2]))