def solution(dartResult):
    length = len(dartResult)

    answer = []

    bonus=""
    temp=[]
    before=0
    Num=0
    tempNum = ''
    for i in range(length):

        if dartResult[i] == "*" or dartResult[i] == "#":
            continue
        if dartResult[i].isdigit():
            tempNum+=dartResult[i]
        elif dartResult[i] =="S" or dartResult[i]=="D" or dartResult[i]=="T":
            Num=int(tempNum)
            if dartResult[i] =="S":
                Num = Num**1
            elif dartResult[i] == "D":
                Num = Num **2
            elif dartResult[i] =="T":
                Num=Num**3

            if i+1<length:
                if dartResult[i+1]=="*":
                    Num*=2
                    if answer:
                        answer[-1] = answer[-1]*2
                elif dartResult[i+1]=="#":
                    Num*=-1
            answer.append(Num)
            tempNum=''
            #print(answer)
    return sum(answer)


print(solution("1S2D*3T"))