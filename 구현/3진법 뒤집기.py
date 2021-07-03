
def solution(n):
    answer = ''
    result=0
    while n>0:
        answer+=str(n%3)
        n=n//3
    answer=answer[::-1]
    for i in range(len(answer)):
        result+=int(answer[i])*(3**i)

    return result



print(solution(45))
print(solution(125))