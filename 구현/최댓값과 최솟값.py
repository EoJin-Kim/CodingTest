def solution(s):
    answer = []
    s=list(map(int,s.split(" ")))

    answer.append(min(s))
    answer.append(max(s))

    return str(answer[0])+" "+str(answer[1])

print(solution("1 2 3 4"))
