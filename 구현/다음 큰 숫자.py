def solution(n):

    num1=n
    num1= bin(num1)[2:]
    num1=list(num1)
    cnt1=num1.count("1")

    while True:
        n+=1
        num2 = bin(n)[2:]
        num2 = list(num2)
        cnt2 = num2.count("1")
        if cnt1==cnt2:
            break
    return n


print(solution(15))

