def solution(a, b):
    if a == b:
        return a

    temp = a + b
    if a > b:

        return temp*(a-b+1)//2
    else:
        return temp * (b - a + 1)// 2


print(solution(1,10))
print(solution(-1,-10))
print(solution(3,5))