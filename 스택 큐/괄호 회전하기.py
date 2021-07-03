
op = ["(", "[", "{"]
cl = [")", "]", "}"]
def solution(s):
    answer = 0
    length = len(s)
    for i in range(length):
        if CheckStr(i, s):
            answer += 1

    return answer


def CheckStr(i, s):

    stack = []
    s = s[i:] + s[:i]
    for x in s:
        if x in op:
            stack.append(x)
        else:
            if not stack:
                return False
            if op.index(stack[-1]) == cl.index(x):
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True


print(solution("[](){}"))
print(solution("}]()[{"))
