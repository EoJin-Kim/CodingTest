name_dict = {}
def DFS(seller,price,answer):
    pay_1 = price // 10
    pay_9 = price-pay_1
    answer[name_dict[seller][0]] +=pay_9
    master = name_dict[seller][1]
    if master == "-" or price<10:
        return
    else:
        DFS(name_dict[seller][1],pay_1,answer)



def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)

    for i in range(len(enroll)):
        name_dict[enroll[i]]=[i]
        name_dict[enroll[i]].append(referral[i])

    for i in range(len(seller)):
        DFS(seller[i],amount[i]*100,answer)

    return answer




print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10]))
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],	["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["john", "john"], [10, 15]))
#print(solution(["john"],	["-"], ["john", "john"], [10, 15]))