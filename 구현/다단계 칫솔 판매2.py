
dic = {}


def DFS(seller, amount,answer):
    global dic
    amount_01 = amount //10
    amount_09 = amount - amount_01

    if seller[0] == "-":
        return
    idx = dic[seller][0]
    if amount < 10:
        answer[idx] += amount
    else:
        answer[idx] += amount_09
        DFS(dic[seller][1], amount_01,answer)

def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)

    for i in range(len(enroll)):
        dic[enroll[i]] = [i]

    for i in range(len(referral)):
        dic[enroll[i]].append(referral[i])

    for i in range(len(seller)):
        DFS(seller[i], amount[i] * 100,answer)

    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10]))