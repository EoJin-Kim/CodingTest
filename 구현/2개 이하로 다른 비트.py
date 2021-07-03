def solution(numbers):
    answer = []

    for num in numbers:
        num = bin(num)[2:]
        cnt0 = num.count("0")
        if cnt0:
            num = list(num)
            last1idx = None
            for i in range(len(num) - 1, -1, -1):
                if num[i] == "0":
                    num[i] = "1"
                    if last1idx != None:
                        num[last1idx]="0"
                    num = "".join(num)
                    break
                else:
                    last1idx = i


        else:
            num = "10" + num[1:]

        answer.append(int(num, 2))
        # print(num)

    return answer


print(solution([0, 5, 2, 7]))
