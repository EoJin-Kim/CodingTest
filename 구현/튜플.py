def solution(s):
    s=s[1:-1]

    answer = []
    tmp = []
    tp=[]
    tpStr=""
    for i in s:
        if i=="}":
            tp.append(int(tpStr))
            tmp.append(tp)
            tp=[]
            tpStr=""
        if i=="," and tpStr:
            tp.append(int(tpStr))
            tpStr=""
        if i.isalnum():
            tpStr+=i



    # 가장 길이 큰 배열
    maxList=[]
    for i in tmp:
        if len(i)>len(maxList):
            maxList=i

    while True:
        if not tmp:
            break
        for x in maxList:
            if not NumCheck(tmp,x):
                continue
            answer.append(x)
            newTmp=[]
            for i in range(len(tmp)):
                tmp[i].remove(x)
                if tmp[i]:
                    newTmp.append(tmp[i])
            tmp = newTmp
            break
    return answer

def NumCheck(array,x):
    for i in array:
        if not x in i:
            return False
    return True

print(solution(	"{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution(	"{{20,111},{111}}"))