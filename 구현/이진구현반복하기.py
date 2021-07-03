def solution(s):


    count=0
    round=0
    while True:
        cnt1 = s.count("1")
        cnt0 = s.count("0")
        if cnt1==1 and cnt0==0:
            break
        round+=1
        count+=cnt0
        s=bin(cnt1)[2:]


    return [round,count]


print(solution("110010101001"))