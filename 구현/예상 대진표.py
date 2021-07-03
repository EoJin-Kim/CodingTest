
def solution(n,a,b):
    answer = 0
    while True:
        if abs(a-b)==1 and max([a,b])%2==0:
            return answer+1
        if a%2==0:
            a=a//2
        else:
            a=a//2+1
        if b%2==0:
            b=b//2
        else:
            b=b//2+1
        answer+=1
    return answer

print(solution(8,4,7))