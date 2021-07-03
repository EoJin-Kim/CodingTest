def solution(n, t, m, p):
    answer = ''
    number=0
    nCount=0
    check=False
    while True:
        numStr=ConvertN(number,n)
        for x in numStr:
            nCount+=1
            if nCount==p:
                answer+=x
                if len(answer)==t:
                    check=True
                    break
            if nCount==m:
                nCount=0
        if check==True:
            break
        number+=1
    return answer

def ConvertN(num,n):
    if num==0:
        return "0"
    result=""
    while num!=0:
        remain=str(num%n)
        if remain=="10":
            remain="A"
        elif remain=="11":
            remain="B"
        elif remain == "12":
            remain = "C"
        elif remain == "13":
            remain = "D"
        elif remain == "14":
            remain = "E"
        elif remain == "15":
            remain = "F"

        result+=remain
        num=num//n

    return result[::-1]


print(solution(2,4,2,1))
print(solution(16,16,2,1))