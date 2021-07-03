def solution(numbers):
    numbers = list(map(str, numbers))

    numbers.sort(key=SortFunc, reverse=True)
    return str(int(''.join(numbers)))

def SortFunc(number):
    return number*4
print(solution([3, 30, 34, 5, 9]))


6666
6161