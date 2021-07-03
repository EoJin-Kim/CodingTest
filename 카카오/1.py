
dictArray={"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
def solution(s):
    answer = ""
    numStr=""
    for i in s:
        if i.isdigit():
            answer+=i
        else:
            numStr+=i
            if dictArray.get(numStr):
                answer+=dictArray[numStr]
                numStr=""

    return int(answer)

print(solution("one4seveneight"))