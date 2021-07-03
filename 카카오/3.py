from collections import Counter

def solution(n, k, cmd):

    deletStack=[]
    array=[i for i in range(n)]


    for opers in cmd:
        if opers[0]=="U" or opers[0]=="D":
            oper,num = opers.split()
            # U일 경우 위로 이동
            if oper=="U":
                k=k-int(num)
            # D일 경우 아래로 이동
            else:
                k=k+int(num)


        # C 일 경우 삭제
        elif opers=="C":
            deletStack.append((k,array[k]))
            array.pop(k)
            if k==len(array):
                k-=1

        # Z 일 경우
        else:
            if deletStack:
                array.insert(deletStack[-1][0],deletStack[-1][1])
                if k>=deletStack[-1][0]:
                    k+=1

                deletStack.pop()

            #print(opers)

    answer = ["O"] * n
    for i in deletStack:
        answer[i[1]]="X"
    return "".join(answer)
    '''
    answer = ''
    
    arrayCounter=Counter(array)
    for i in range(n):
        if arrayCounter.get(i):
            answer+="O"
        else:
            answer+="X"
    print(answer)
    
    
    start=0
    for i in array:
        if start==i:
            answer+="O"
            start+=1

        else:
            answer+="X"*(i-start)
            answer+="O"
            start=i+1
    return answer
    '''
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))