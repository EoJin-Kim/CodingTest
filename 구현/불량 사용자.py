
from itertools import product

def solution(user_id, banned_id):

    len_table={}
    for i in range(1,9):
        len_table[i]=[]
    for uid in user_id:
        len_table[len(uid)].append(uid)

    result=[]
    for bid in banned_id:
        temp=[]
        for uid in len_table[len(bid)]:
            check=True
            for b,u in zip(bid,uid):
                if b=="*" or b==u:
                    continue
                check=False
            if check:
                temp.append(uid)
        result.append(temp)
        temp=[]

    length=len(result)
    answer=[]
    totalList=list(product(*result))
    for i in totalList:
        temp=set(i)
        if len(temp)!=length:
            continue
        if not temp in answer:
            answer.append(temp)

    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))