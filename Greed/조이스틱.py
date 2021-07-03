# alpha={"A":1,"B":2,"C":3,"D":4","D"}

# 위아래 거리 찾기(양방향 중 짧은 거리)
# 좌우 거리 찾기(양방향 중 짧은 거리)
# 위 두개중 가장 짧은 거리
# print(ord("A")) = 65
# print(ord("Z")) = 90
'''
def solution(name):
    answer = 0
    answerStr = ["A"]*len(name)
    for i in range(len(name)):
        mindis = 100
        for j in range(len(answerStr)):
            dis1 = ord(answerStr[j])
            if ord(name[i]) < ord(answerStr[j]):
                dis2 = ord(answerStr[j]) - 26
            else:
                dis2 = ord(answerStr[j]) + 26
            mindis = min(abs(ord(name[i])-dis1)+abs(j-i), abs(ord(name[i])-dis2)+abs(j-i), mindis)
        dis3 =ord(name[i]) -ord("A")
        dis4=ord("A") - (ord(name[i])-26)
        answer+=min(mindis,dis3,dis4)
    return answer

'''
def solution(name):
    make_name = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
    print(make_name)

    idx, answer = 0, 0
    while True:
        answer += make_name[idx]
        make_name[idx] = 0
        if sum(make_name) ==0:
            break
        left, right = 1, 1
        while make_name[idx - left] ==0:
            left +=1
        while make_name[idx + right] ==0:
            right +=1

        if left<right:
            answer+=left
            idx += -left
        else:
            answer+=right
            idx += right




    return answer

#print(solution("JAN"))
#print(solution("JAZ"))
print(solution("JAAJN"))
