def solution(n):
    cnt=0
    while n!=0:
        if n%2==0:
            n=n//2
        else:
            cnt+=1
            n=(n-1)//2
    return cnt


print(solution(5))
print(solution(6))
print(solution(5000))