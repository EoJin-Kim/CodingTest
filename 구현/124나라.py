def solution(n):
    num = ["4", '1', '2']
    answer = ""
    while n:
        answer = num[n % 3] + answer
        if n % 3 == 0:
            n = n // 3 - 1
        else:
            n = n // 3
            size
    return answer
print(solution(6))
print(solution(4))
print(solution(3))
print(solution(10))