def solution(s):
    answer = True
    stack=[]
    for x in s:
        if x=="(":
            stack.append(x)
        else:
            if not stack:
                answer=False
                break
            if stack[-1]=="(":
                stack.pop()

            else:
                answer=False
                break

    if stack:
        answer=False
        return answer

    return answer
print(solution(")()("))