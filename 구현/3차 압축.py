def solution(msg):
    answer = []
    dic={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17 ,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
    idx=26
    tmp=""
    for m in msg:
        tmp+=m
        if dic.get(tmp):
            continue
        else:
            answer.append(dic[tmp[:-1]])
            #answer.append(dic[tmp[-1]])
            idx+=1
            dic[tmp]=idx
            tmp=tmp[-1]


    if tmp:
        answer.append(dic[tmp])
    return answer


#print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))