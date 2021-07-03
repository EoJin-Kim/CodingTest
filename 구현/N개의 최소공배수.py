import math

def solution(arr):
    answer = arr[0]
    for a in arr[1:]:
        gd=math.gcd(answer,a)
        answer=answer*a//gd

    return answer

print(solution([2,6,8,14]))