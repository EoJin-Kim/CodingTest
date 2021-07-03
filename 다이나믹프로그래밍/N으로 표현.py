from itertools import permutations
# N의 1~ 8까지 개수로 사칙연산으로 만들 수 있는수
# 사용 하는 연산 + , * , / , 붙이기 (4가지)
def solution(N, number):
    answer = -1
    DP = []

    for i in range(1, 9):
        numbers = set()
        numbers.add(int(str(N) * i))

        for j in range(0, i - 1):
            if j>len(DP)-j-1:
                break
            for x in DP[j]:
                for y in DP[-j- 1]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)

                    if y != 0:
                        numbers.add(x // y)
                    if x !=0:
                        numbers.add(y // x)

        if number in numbers:
            answer = i
            break

        DP.append(numbers)

    return answer

print(solution(5,12))
print(solution(5,26))