def solution(s):
    answer = len(s)
    length=len(s)
    for step in range(1,length//2+1):
        compressed=""
        count=1
        prev=s[:step]
        for i in range(step,length,step):
            if prev==s[i:i+step]:
                count+=1
            else:
                if count>=2:
                    compressed+=str(count)+prev
                else:
                    compressed+=prev
                prev=s[i:i+step]
                count=1
        if count >= 2:
            compressed += str(count) + prev
        else:
            compressed += prev
        compressed
        answer=min(answer,len(compressed))
    return answer


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
