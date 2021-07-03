def solution(s):

    total=[]
    s=s.split(" ")
    for a in s:
        #print(a)
        answer = ''
        for i in range(len(a)):
            if a[i]==" ":
                answer+=" "
                continue
            if i%2==0:
                answer+=a[i].upper()
            else:
                answer+=a[i].lower()
        total.append(answer)
    answer=' '.join(total)
    return answer

print(solution("try  hello world"))