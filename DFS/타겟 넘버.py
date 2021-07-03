from itertools import permutations,product

'''
def solution(numbers, target):
    answer = 0
    length = len(numbers)
    expression = [(0,1) for i in range(length)]
    for exp in product(*expression):
        result=0
        for i in range(length):
            if exp[i]==0:
                result+=-numbers[i]
            else:
                result+=numbers[i]

        if result==target:
            answer+=1


    return answer
'''
answer=0
def solution(numbers, target):
    global answer
    dfs(0,numbers,0,target)
    return answer
def dfs(idx,numbers,temp,target):
    global answer
    length = len(numbers)
    if idx == length and temp==target:
        answer+=1
        return
    if idx==length:
        return

    dfs(idx + 1, numbers, temp - numbers[idx],target)
    dfs(idx + 1, numbers, temp + numbers[idx],target)


print(solution([1, 1, 1, 1, 1],3))