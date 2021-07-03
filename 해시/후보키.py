from itertools import combinations

def solution(relation):
    answer=0
    length = len(relation)
    setLen=len(relation[0])

    cases=[]
    for i in range(1,setLen+1):
        for j in combinations([ z for z in range(setLen)],i):
            cases.append(j)
    final=[]
    #print(cases)
    for case in cases:
        tmp=[tuple(item[key] for key in case) for item in relation]

        #print(tmp)
        if len(set(tmp))==length:
            final.append(case)

    answer=set(final)
    for i in range(len(final)):
        for j in range(i+1,len(final)):
            #print(len(final[i]))
            #print(len(set(final[i]).intersection(set(final[j]))))
            if len(set(final[i]).intersection(set(final[j])))==len(final[i]):
                answer.discard(final[j])


    #print(answer)



    return len(answer)



print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))